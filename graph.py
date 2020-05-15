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

def getAuthorsFromDatabase () :
    """
    Return all authors from articles database

    :params : /
    :returns: (dict) dictionnary of all author with their infos
    """
    i = 0
    dictAuthors = {}
    listAuthors = []
    tree = ET.parse('articles_database.xml')
    root = tree.getroot()
    for article in root.findall('article') : 
        titleArticle = article.find('title').text
        for author in article.findall('./authors/author') :
            authorName = author.find('name').text
            groupName = author.find('group').text
            teamName = author.find('team').text
            memberTypeName = author.find('member_type').text

            dictAuthors[authorName]=dict()
            
            if not skipDoubleAuthor(authorName,listAuthors) :
                listAuthors.append(authorName)
                dictAuthors[authorName]['group']=groupName
                dictAuthors[authorName]['team']=teamName
                dictAuthors[authorName]['member_type']=memberTypeName
    return dictAuthors 
    
def skipDoubleAuthor (author,listAuthors) :
    """
    Check if the author given is already in the list
    
    :params: - author (str) the author name
             - listAuthors (list) list of authors
    :returns: True if author already exists, False otherwise
    """
    tmp = False
    for an_author in listAuthors :
        if author.lower() == an_author.lower():
            tmp = True
    return tmp

def initializeGraph(dictAuthors) :
    """
    Initialize a graph from a list of authors
    
    :params: - dictAuthors (dict) dictionnary of authors
    :returns: a graph
    """
    g = Graph(len(listAuthors))
    for authorName in dictAuthors :
        g.vs['nameAuthor'] = authorName
        g.vs['group'] = dictAuthors[authorName]['group']
        g.vs['team'] = dictAuthors[authorName]['team']
        g.vs['member_type'] = dictAuthors[authorName]['member_type']
    return g

def setArc (g) :
    """
    :params: - g (igraph.Graph) a graph
    :returns: /
    """
    i=0
    subsetAuthors = []
    tree = ET.parse('articles_database.xml')
    root = tree.getroot()
    for article in root.findall('article') : 
        print(i) 
        i = i+1
        for author in article.findall('./authors/author') :
            authorName = author.find('name').text
            subsetAuthors.append(authorName) 
        for actorActual in subsetAuthors :
            for actorTarget in subsetAuthors :
                if actorActual != actorTarget :
                    index1Author = g.vs.find(nameAuthor=actorActual)
                    index2Author = g.vs.find(nameAuthor=actorTarget)
                    if not g.are_connected(index1Author, index2Author) :
                        g.add_edges([(index1Author,index2Author)]) # create edge between the two authors
                        edge_id = g.get_edge(index1Author,index2Author)
                        g.es[edge_id]['articles_title'] = []
                        g.es[edge_id]['articles_title'].append(article.find('title').text)
                        
                    else : # if edge already exists between these two authors
                        edge_id = g.get_edge(index1Author,index2Author)
                        g.es[edge_id]['articles_title'].append(article.find('title').text)     
        subsetAuthors = []

        
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
    """
    i = 0
    dictAuthors = getAuthorsFromDatabase()
    print(len(listAuthors))
    g = initializeGraph(dictAuthors)  
    setArc(g)
    g.write("test.GraphML")
    plot(g)
