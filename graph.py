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
    """
    Return all authors from articles database
    """
    i = 0
    listAuthors = []
    tree = ET.parse('articles_database.xml')
    root = tree.getroot()
    for article in root.findall('article') : 
        titleArticle = article.find('title').text
        for author in article.findall('./authors/author') :
            authorArticle =author.find('name').text
            if skipDoubleAuthor(authorArticle,listAuthors) == False :
                listAuthors.append(authorArticle)
    return listAuthors 
    
def skipDoubleAuthor (author,listAuthors) :
    """
    Check if the author given is already in the list
    
    :params: - author (str) the author name
             - listAuthors (list) list of authors
    :returns: True if author already exists, False otherwise
    """
    tmp = False
    for an_author in listAuthors :
        if author == an_author:
            tmp = True
    return tmp

def initializeGraph(listAuthors) :
    """
    Initialize a graph from a list of authors
    
    :params: - listAuthors (list) list of authors
    :returns: a graph
    """
    g = Graph(len(listAuthors))
    g.vs["nameAuthor"] = listAuthors
    return g

def setArc (g) :
    """
    :params: - g (igraph.Graph) a graph
    :returns: /
    """
    listArtc = []
    i=0
    exist = False
    subset = []
    tree = ET.parse('articles_database.xml')
    root = tree.getroot()
    for article in root.findall('article') : 
        print(i) 
        i = i+1
        for author in article.findall('./authors/author') :
            authorArticle =author.find('name').text
            subset.append(authorArticle) 
        for actorActual in subset :
            for actorTarget in subset :
                if actorActual != actorTarget :
                    index1Author = g.vs.find(nameAuthor=actorActual)
                    index2Author = g.vs.find(nameAuthor=actorTarget)
                    if g.are_connected (index1Author, index2Author) == False :
                        g.add_edges([(index1Author,index2Author)])
        subset = []

        
def ifArcExist(g,index1,index2) :
    """
    """
    test = False
    if g.are_connected (index1, index2) == False :
        test = True
    return test

def main():
    """
    main function
<<<<<<< HEAD
    """
i = 0
ListAuthors = getAuthorsFromDataBase()
print len(ListAuthors)
g = initializeGraph(ListAuthors)  
setArc(g)
g.write("test.GraphML")
plot(g)
