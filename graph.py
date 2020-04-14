import requests
from lxml import etree
import sys
import igraph
from igraph import *
import xml.etree.cElementTree as ET
from decimal import Decimal
import os

def leaveDuplicatAuthors (Author,ListAuthors) :
    test = False
    #if ListAuthors is None :
        #return False
    for author in ListAuthors :
        if Author == author:
            test = True
    return test

def InitializeGraph (ListAuthors) :
    g = Graph(len(ListAuthors))
    g.vs["nameAuthor"] = ListAuthors
    for i in range (0,len(ListAuthors)):
        print g.vs[i]["nameAuthor"]

def getAuthorsFromDataBase () :
    ListAuthors = []
    tree = ET.parse('articles_database.xml')
    root = tree.getroot()
    for article in root.findall('article') : 
        titleArticle = article.find('title').text
        for author in article.findall('./authors/author') :
            authorArticle =author.find('name').text
            if leaveDuplicatAuthors(authorArticle,ListAuthors) == False :
                ListAuthors.append(authorArticle) 
    return ListAuthors   
             
def main():
    """
    main function
    """
    ListAuthors = getAuthorsFromDataBase()
    #print len(ListAuthors)
    InitializeGraph(ListAuthors)       
     
       
        
   
#g = Graph([(0,1), (0,2), (2,3), (3,4), (4,2), (2,5), (5,0), (6,3), (5,6)])
#g.vs
#g.vs["name"] = ["Alice", "Bob", "Claire", "Dennis", "Esther", "Frank", "George"]
#g.vs["age"] = [25, 31, 18, 47, 22, 23, 50]
#g.vs["gender"] = ["f", "m", "f", "m", "f", "m", "m"]
#g.es["is_formal"] = [False, False, True, True, True, False, True, False, False]
#g.edge_betweenness()
#layout = g.layout_kamada_kawai()
#layout = g.layout("kamada_kawai")
#layout = g.layout("kk")
#plot(g,layout = layout)
#g.save("test.GraphML")

if __name__ == "__main__":
    # execute only if run as a script
    main()
