#!/usr/bin/python                                                                       
# -*- coding: utf-8 -*- 
import requests
from lxml import etree
import sys
import igraph
from igraph import *
import xml.etree.cElementTree as ET
from decimal import Decimal
import os
from unidecode import unidecode
from networkx import nx



def getAuthorsFromDataBase () :
    i = 0
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
    return g

def setArc (g,author) :
    i=0
    exist = False
    subset = []
    tree = ET.parse('articles_database.xml')
    root = tree.getroot()
    for article in root.findall('article') : 
        for author in article.findall('./authors/author') :
            authorArticle =author.find('name').text
            subset.append(authorArticle) 
        for authorBySubSet in subset :
            if authorBySubSet == author :
                exist = True 
        if exist == True :
            for authorBySubSet in subset :
                if authorBySubSet != author :
                    index1Author = g.vs.find(nameAuthor=author)
                    index2Author = g.vs.find(nameAuthor=authorBySubSet)
                    if ifArcExist(g,index1Author,index2Author) == True :
                        g.add_edges([(index1Author,index2Author)])
        subset = []

        
def ifArcExist(g,index1,index2) :
    test = False
    if g.are_connected (index1, index2) == False :
        test = True
    return test

def main():
    """
    main function
    """
i = 0
ListAuthors = getAuthorsFromDataBase()
g = InitializeGraph(ListAuthors)  
#for author in ListAuthors :
    #print "auteur N ",i
    #i = i+1
    #setArc(g,author)
#g.export("test.xml")
g.save("test.GraphML")
layout = g.layout_kamada_kawai()
layout = g.layout("kamada_kawai")
layout = g.layout("kk")
plot(g,layout = layout)

        
   
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
