import requests
from lxml import etree
import xml.etree.cElementTree as ET
import html
from decimal import Decimal
import os
import check_names


def get_articles_by_author(author,cristal_members={}):
    """
    GET informations about all articles where the author is involved

    :params : - author (str) the author name
              - cristal_members (dict) all cristal members (default={})
    :returns: (list) list of all articles where the author is involved

    """
    res=[]
    GET_URL="https://api.crossref.org/works"
    response=requests.get(GET_URL+'?query.author='+author+'&mailto=mael.avennec.etu@univ-lille.fr')
    response=response.json()

    items=response['message']['items']

    i=0
    for item in items:
        tmp={}
        # publisher
        if 'publisher' in item :
            publisher=item['publisher']
            tmp['publisher']=html.unescape(publisher)
        # type
        if 'type' in item : 
            document_type=item['type']
            tmp['type']=html.unescape(document_type)
        else :
            tmp['type']='unknown'
        # title
        if 'title' in item :
            title=item['title'][0]
            tmp['title']=html.unescape(title)
        else :
            tmp['title']="No Title"
        # authors
        authors=[]
        for author in item['author']:
            author_array=[]
            # author name
            if 'given' in author :
                author_name=author['given']
                if 'family' in author :
                    author_name+=' '+author['family']
            else :
                if 'family' in author :
                    author_name = author['family']
                else :
                    author_name = author['name']
            author_array.append(html.unescape(author_name))
            # author affiliation
            if 'affiliation' in author :
                if 'name' in author['affiliation'] :
                    author_array.append(author['affiliation']['name']) # affiliation
                    author_array.append('Unknown') # group
                    author_array.append('Unknown') # team
                    author_array.append('Unknown') # member type
                else :
                    if author_array[0] in cristal_members:
                        author_array.append('CRIStAL') # affiliation
                        author_array.append(cristal_members[author_array[0]]['group']) # group
                        author_array.append(cristal_members[author_array[0]]['team']) # team
                        author_array.append(cristal_members[author_array[0]]['member_type']) # member type
                    else :
                        author_array.append('Unknown') # affiliation
                        author_array.append('Unknown') # group
                        author_array.append('Unknown') # team
                        author_array.append('Unknown') # member type
            else :
                if author_array[0] in cristal_members:
                    author_array.append('CRIStAL') # affiliation
                    author_array.append(cristal_members[author_array[0]]['group']) # group
                    author_array.append(cristal_members[author_array[0]]['team']) # team
                    author_array.append(cristal_members[author_array[0]]['member_type']) # member type

                else :
                    author_array.append('Unknown') # affiliation
                    author_array.append('Unknown') # group
                    author_array.append('Unknown') # team
                    author_array.append('Unknown') # member type
            authors.append(author_array)
        tmp['authors']=authors
        # abstract
        if 'abstract' in item :
            abstract = item['abstract']
            tmp['abstract']=html.unescape(abstract)
        # url  
        url=item['URL']
        tmp['url']=html.unescape(url)
        
        res.append(tmp)
    return res

def test_author_by_name(author, publication):
    """
    Test if the name of the search is an author of the publication

    :params: - author (str)
             - publication (dict)
    :returns: (bool) True if it's an author of th publication, False otherwise

    :example:
    
    """
    test = False 
    for auteur in publication['authors']:
        if (auteur[0] == author):
            test = True
    return test

def test_article_already_exists(publication) :
    """
    Test if the article is already in the database
    
    :params: - publication (dict) a publication
    :returns: (bool) True if article already exsits, False otherwise
    """
    test = False
    if os.stat('articles_database.xml').st_size == 0 :
        return test
    tree = ET.parse('articles_database.xml')
    root = tree.getroot()
    for article in root.findall('article') :
        titleArticle = article.find('title').text

        if publication['title'] == titleArticle :
            test = True
    return test

def save_articles_into_database(publications,the_author,verbose=False):
    """
    Save the publication into database

    :params: - publications (list) list of publications
             - the_author (str) the author name
             - verbose (bool) {default = False} True to active the verbose mode, False otherwise 
    :returns: /
    """
    newArticles = 0
    
    articles = etree.Element("articles") # create the main tag

    for publication in publications :
        if test_author_by_name(the_author,publication) == True and test_article_already_exists(publication) != True:
            
            article = etree.SubElement(articles, "article")
            # reference
            reference = etree.SubElement(article, "reference")
            reference.text = "Crossref"
            # title
            title = etree.SubElement(article,"title")
            title.text = publication['title']
            # publisher
            if 'publisher' in publication : 
                publisher = etree.SubElement(article, "publisher")
                publisher.text = (publication['publisher'])
            # authors
            authors = etree.SubElement(article, "authors")
            for author_arr in publication['authors'] :
                # author
                author = etree.SubElement(authors,"author")
                nom = etree.SubElement(author, "name")
                affiliation = etree.SubElement(author,"affiliation")
                group = etree.SubElement(author,"group")
                team = etree.SubElement(author,"team")
                member_type = etree.SubElement(author,"member_type")
                nom.text = check_names.check_name(author_arr[0]) # replace letters with accents and/or replace name if exists in list of similar names 
                affiliation.text = author_arr[1]
                group.text = author_arr[2]
                team.text = author_arr[3]
                member_type.text = author_arr[4]
            # abstract
            if 'abstract' in publication : 
                abstract = etree.SubElement(article,'abstract')
                abstract.text = publication['abstract']
            # type    
            type_article = etree.SubElement(article,"type") 
            type_article.text=publication['type']
            # url
            url = etree.SubElement(article,"URL")
            url.text = publication['url']

            newArticles+=1 # increments the counter of new articles added

            if os.stat('articles_database.xml').st_size != 0 : # if the database file is not empty
                fichier = open("articles_database.xml", "r") 
                lines = fichier.readlines()
                fichier.close()
                
                taille = len(lines)
                lines[taille-1]="" # delete the last line of the file ( </articles> )
                
                fichier = open ("articles_database.xml","w")
                fichier.writelines(lines) # rewrite the entire file without last line
                fichier.close()

                fichier = open("articles_database.xml","a")
                fichier.write(etree.tostring(article, encoding='unicode', pretty_print=True))
                fichier.write("</articles>") # add the last line to close the tag
                fichier.close()
            else : # if the database file is empty
                fichier = open("articles_database.xml","a")
                fichier.write(etree.tostring(articles, encoding='unicode', pretty_print=True))
                fichier.close()
            
            

    if verbose == True :
        print('Base de donnée :\n----------------')
        print(str(newArticles)+" nouveaux articles ont été ajoutés à la base de données <articles_database.xml> ")

def display_publications(publications,author):
    """
    Display publications of an author in textual format

    :params: - publications (list) list of publications
             - author (str) the author name
    :returns: /
    """
    res="***"+22*'*'+len(author)*'*'+'**\n'
    res+="** Les publication pour " + author + " **\n"
    res+="***"+22*'*'+len(author)*'*'+'**\n\n'
    i=0
    for publication in publications :
        res+="# Publication numéro "+str(i)+"\n\n"
        res+="Titre : " + publication['title'] + "\n"
        res+="Auteurs : "+publication['authors'][0]
        for author in publication['authors'][1:] :
            res+=', '+author
        res+="\n"
        res+="Publié par : "+ publication['publisher'] + "\n"
        res+="Type : "+ publication['type'] + "\n"
        res+="URL : " + publication['url'] + "\n"
        res+="\n"
        i+=1
    print(res)

def test_accuracy_author_name(author,publications,verbose=False):
    """
    Test the accuracy of the API about the author name, to know if the publication got the right author name

    :params: - author (str) the author name
             - publications (list) list of publications
             - verbose (bool) {default = False} True to active the verbose mode, False otherwise 

    :returns: /
    """
    identique = 0
    nonIdentique = 0
    
    for publication in publications :
        for auteur in publication['authors']:
            if (auteur[0] == author):
                identique += 1
    nonIdentique = len(publications) - identique

    if len(publications) == 0 :
        error_rate = 0
    else :
        error_rate=Decimal(nonIdentique) / Decimal(len(publications)) *100

    if verbose == True :
        print("\nPrécision sur l'auteur :\n------------------------")
        print(str(identique) ,"articles possède le nom d'autheur : '"+author+"' et ",nonIdentique,"articles ne le possèdent pas")
        print("> Taux d'erreur = ", error_rate,"%")

            
def main():
    """
    main function
    """
    print("------------\n| Crossref |\n------------\n")
    
    AUTHOR='Laetitia Jourdan'
    publications=get_articles_by_author(AUTHOR)

    save_articles_into_database(publications,AUTHOR,True)
    #display_publications(publications,AUTHOR)
    test_accuracy_author_name(AUTHOR, publications,True)
    

if __name__ == "__main__":
    # execute only if run as a script
    main()
