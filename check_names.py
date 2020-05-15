#!/usr/bin/python                                                                       
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import re
import unicodedata
import numpy as np

names={'leatitia jourdan-vermeulen':'Leatitia Jourdan',
       'remy gilleron':'remi gilleron',
       'belkacem ould bouamama':'Belkacem Ould-Bouamama',
       'belkacem ould bouamam':'Belkacem Ould-Bouamama',
       'xaiver le pallec':'Xavier Le Pallec',
       'el ghazali talbi':'El-Ghazali Talbi',
       'ei-ghazali taibi':'El-Ghazali Talbi',
       'nicolas durand 0001':'Nicolas Durand'
       }

def check_name(name):
    """
    """
    if strip_accents(name.lower()) in names :
        print('Name to change : '+name)
        return names[strip_accents(name.lower())]
    return strip_accents(name)


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

def hamming_distance(chaine1, chaine2):
    """
    """
    return len(list(filter(lambda x : ord(x[0])^ord(x[1]), zip(chaine1, chaine2))))

def strip_accents(text):
    """
    Strip accents from input String.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)

def check_all_authors_name_database(distance_max):
    authors_found_checked=[]
    
    tree = ET.parse('articles_database.xml')
    root = tree.getroot()
    for authorActual in root.findall('article/authors/author/name') :
        authorArticleActual=strip_accents(authorActual.text) # remove accents
            
        for authorTarget in root.findall('article/authors/author/name') : 
            authorArticleTarget=strip_accents(authorTarget.text) # remove accents

            if(authorArticleActual != authorArticleTarget):
                couple_actual_target = set()
                couple_actual_target.add(authorArticleActual)
                couple_actual_target.add(authorArticleTarget)

                if(couple_actual_target not in authors_found_checked):
                    if(0 < hamming_distance(authorArticleActual.lower(), authorArticleTarget.lower()) <= distance_max):
                        print('Actual : '+authorArticleActual+', Target : '+authorArticleTarget)
                        authors_found_checked.append(couple_actual_target) # add the new couple found in the list of couple already found



    

def main():
    """
    main function
    """
    #print(check_all_authors_name_database(1))
    print(check_name('Laetitia Vermeulen-Jourdan'))


if __name__ == "__main__":
    # execute only if run as a script
    main()
    
