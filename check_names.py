#!/usr/bin/python                                                                       
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET

names={'leatitia jourdan-vermeulen':'Leatitia Jourdan',
       }

import numpy as np

def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    print (matrix)
    return (matrix[size_x - 1, size_y - 1])

def check_name(name):
    """
    """
    if name.lower() in names :
        return names[name]
    return name

def hamming_distance(chaine1, chaine2):
    return len(list(filter(lambda x : ord(x[0])^ord(x[1]), zip(chaine1, chaine2))))

def check_all_authors_name_database():
    author_checked=[]
    
    tree = ET.parse('articles_database.xml')
    root = tree.getroot()
    for authorActual in root.findall('article/authors/author/name') :
        authorArticleActual=authorActual.text
            
        for authorTarget in root.findall('article/authors/author/name') : 
            authorArticleTarget=authorTarget.text

            if(hamming_distance(authorArticleActual.lower(), authorArticleTarget.lower())==1):
                print('Actual : '+authorArticleActual+', Target : '+authorArticleTarget) 
    

def main():
    """
    main function
    """
    #unify_name('Leatitia Jourdan')
    #levenshtein('mael','mael')
    print(check_all_authors_name_database())


if __name__ == "__main__":
    # execute only if run as a script
    main()
    
