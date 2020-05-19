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
            affiliationName = author.find('affiliation').text
            groupName = author.find('group').text
            teamName = author.find('team').text
            memberTypeName = author.find('member_type').text
            
            if skipDoubleAuthor(authorName.lower(),listAuthors) == False:
                listAuthors.append(authorName.lower())
                dictAuthors[authorName.lower()]=dict()
                dictAuthors[authorName.lower()]['name']=authorName
                dictAuthors[authorName.lower()]['affiliation']=affiliationName
                dictAuthors[authorName.lower()]['group']=groupName
                dictAuthors[authorName.lower()]['team']=teamName
                dictAuthors[authorName.lower()]['member_type']=memberTypeName
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
    g = Graph(len(dictAuthors))
    names = []
    affiliations =[]
    groups = []
    teams = []
    member_types = []
    for authorName in dictAuthors :
        names.append(dictAuthors[authorName]['name'])
        affiliations.append(dictAuthors[authorName]['affiliation'])
        groups.append(dictAuthors[authorName]['group'])
        teams.append(dictAuthors[authorName]['team'])
        member_types.append(dictAuthors[authorName]['member_type'])

    g.vs['nameAuthor']=names
    g.vs['affiliation']=affiliations
    g.vs['group']=groups
    g.vs['team']=teams
    g.vs['member_type']=member_types
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
        i = i+1
        for author in article.findall('./authors/author') :
            authorName = author.find('name').text
            subsetAuthors.append(authorName)
        coupleAuthorsChecked=[]
        for actorActual in subsetAuthors :
            for actorTarget in subsetAuthors :
                if actorActual != actorTarget :
                    
                    coupleAuthors=set()
                    coupleAuthors.add(actorActual)
                    coupleAuthors.add(actorTarget)
                    
                    index1Author = g.vs.find(nameAuthor=actorActual)
                    index2Author = g.vs.find(nameAuthor=actorTarget)
                    if not g.are_connected(index1Author, index2Author) :
                        g.add_edges([(index1Author,index2Author)]) # create edge between the two authors
                        edge_id = g.get_eid(index1Author,index2Author)
                        g.es[edge_id]['articles_nb']=0
                        g.es[edge_id]['article_title_'+str(g.es[edge_id]['articles_nb'])]=article.find('title').text
                        g.es[edge_id]['articles_nb']+=1
                        
                    else : # if edge already exists between these two authors
                        if(coupleAuthors not in coupleAuthorsChecked): # to escape doublon in article title
                        
                            edge_id = g.get_eid(index1Author,index2Author)

                            g.es[edge_id]['article_title_'+str(g.es[edge_id]['articles_nb'])]=article.find('title').text   
                            g.es[edge_id]['articles_nb']+=1
                            
                    coupleAuthorsChecked.append(coupleAuthors)
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
    filename = "graph.GraphML"
    i = 0
    print('Récupération des auteurs dans la base de donnée...\n')
    dictAuthors = getAuthorsFromDatabase()
    print('Initialisation du graphe...\n')
    g = initializeGraph(dictAuthors)
    print('Ajout des arcs...\n')
    setArc(g)
    print('Ecriture dans le fichier (',filename,')...\n')
    g.write(filename)

if __name__ == "__main__": # execute only if run as a script
    main()

