#!/usr/bin/python                                                                       
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import re
import unicodedata
import numpy as np

names={'Laetitia Jourdan-Vermeulen':'Laetitia Jourdan',
       'Remy Gilleron':'Remi Gilleron',
       'Belkacem Ould-Bouamama':'Belkacem Ould Bouamama',
       'Belkacem Ould-Bouamam':'Belkacem Ould Bouamama',
       'Xaiver Le Pallec':'Xavier Le Pallec',
       'El-Ghazali Talbi':'El Ghazali Talbi',
       'Ei-Ghazali Taibi':'El Ghazali Talbi',
       'Nicolas Durand 0001':'Nicolas Durand',
       'Simon Collart-Dutilleul' : 'Simon Collart Dutilleul',
       'Adnen El-Amraoui' : 'Adnen El Amraoui',
       'Anne-Cecile Caron' : 'Anne Cecile Caron',
       'Jean-Pierre Bourey' : 'Jean Pierre Bourey',
       'Ismahene Hakj Khalifa' : 'Ismahene Hadj Khalifa',
       'Loan Marius Bilasco' : 'Ioan Marius Bilasco',
       'Juan Carlos Elvarez Paiva' : 'Juan Carlos Alvarez Paiva',
       'Hong-Phuong Dang' : 'Hong Phuong Dang',
       'Jean-Michel Charbois' : 'Jean Michel Charbois',
       'Marcos Eduardo Gomes-Borges' : 'Marcos Eduardo Gomes Borges',
       'Jean-Francois Coeurjolly' : 'Jean Francois Coeurjolly',
       'Thierry-Marie Guerra' : 'Thierry Marie Guerra',
       'Jean-Pierre Barbot' : 'Jean Pierre Barbot',
       'Silviu-Iulian Niculescu' : 'Silviu Iulian Niculescu',
       'Andrey Polyakov 0001' : 'Andrey Polyakov',
       'Andrei Polyakov 0001' : 'Andrey Polyakov',
       'Tatiana Kharkovskaya' : 'Tatiana Kharkovskaia',
       'Alireza Fakhrizadeh Esfahani' : 'Alireza Esfahani',
       'Jian Zhang 0042' : 'Jian Zhang'
       }

def check_name(name):
    """
    Check the name

    :param: - name (str) a name
    :return: (str) the name unify without accent and only first letter of each name to upper

    :example:
    >>> check_name('Belkacem Ould-Bouamama')
    Belkacem Ould Bouamama
    """
    if strip_accents(name) in names :
        return str_to_capitalize_without_dashes(names[strip_accents(name)])
    return str_to_capitalize_without_dashes(strip_accents(name))

def str_to_capitalize_without_dashes(string):
    """
    To unify the string

    :params: - string (str) a string
    :returns: (str) a string with first letter of each word to capitalize

    :examples:
    >>> str_to_capitalize_without_dashes('hello world')
    'Hello World'
    >>> str_to_capitalize_without_dashes('hello woRLd')
    'Hello World'
    >>> str_to_capitalize_without_dashes('HELLO woRLd')
    'Hello World'
    >>> str_to_capitalize_without_dashes('HELLO woRLd 01')
    'Hello World 01'
    >>> str_to_capitalize_without_dashes('hello world-hello')
    'Hello World Hello'
    """
    tab=re.findall(r"[\w\.\']+",string)
    res=[]
    for w in tab :
        res.append(w.capitalize())
    return ' '.join(res)


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

def hamming_distance(string1, string2):
    """
    Calculate the distance between two string

    :params: - string1 (str) The first string
             - string2 (str) The second string
    :returns: (int) the distance between the two string

    :example:
    >>> hamming_distance('hello world','hello world')
    0
    >>> hamming_distance('hello world','hello-world')
    1
    >>> hamming_distance('hello world','helloworld')
    5
    >>> hamming_distance('hello world','hello world !')
    0
    """
    return len(list(filter(lambda x : ord(x[0])^ord(x[1]), zip(string1, string2))))

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
    """
    Check and display authors who have a distance max less or equal to the parameter distance_max

    :param: - distance_max (int) the distance maximum
    :return: /

    :example:
    >>> check_all_authors_name_database(1)
    Olivier Gauwin <-> Olivier Bau
    Remi Gilleron <-> Remy Gilleron
    ...
    """
    
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
                    if(0 < hamming_distance(authorArticleActual, authorArticleTarget) <= distance_max):
                        print(authorArticleActual+' <-> '+authorArticleTarget)
                        authors_found_checked.append(couple_actual_target) # add the new couple found in the list of couple already found

def main():
    """
    main function
    """
    print(check_all_authors_name_database(1))
    #print(check_name('Laetitia Vermeulen-Jourdan'))


if __name__ == "__main__":
    # execute only if run as a script
    main()
    
