import requests
from lxml import etree
import sys
import xml.etree.cElementTree as ET


def get_publications_by_author(author,h=30):
    """
    GET informations about all publications where the auhtor is involved

    :params : - author (str) the author name
              - h (int) number max of results (default = 30)
    :returns: (list) list of all publications where the author is involved

    """
    res=[]
    GET_URL="http://dblp.org/search/publ/api"
    response=requests.get(GET_URL+'?q='+author+'&h='+str(h)+'&format=json')
    response=response.json()

    nb_hits=response['result']['hits']['@total']

    hits=response['result']['hits']['hit']

    for hit in hits :
        tmp={}
        # title
        title=hit['info']['title']
        tmp['title']=title
        # type
        document_type=hit['info']['type']
        tmp['type']=document_type
        # authors'
        authors=[]
        for author in hit['info']['authors']['author']:
            author_name=author['text']
            authors.append(author_name)
        tmp['authors']=authors
        # url
        url=hit['info']['ee']
        tmp['url']=url
        
        res.append(tmp)

    return res


def test_auteur_by_name(author,res):   
    test = False 
    for auteur in res['authors']:
        if (auteur == author):
            test = True
    return test

def ifExists(res) :
    test = False
    tree = ET.parse('result.xml')
    root = tree.getroot()
    for titre in root.findall('article') :
        titreArticle = titre.find('Titre').text
        print titreArticle
        if res['title'] == titreArticle :
            test = True
    return test

def main():
    """
    main function
    """
    AUTHOR='Laetitia Jourdan'

    articles = etree.Element("Articles")

    for res in get_publications_by_author(AUTHOR) :
        if test_auteur_by_name(AUTHOR,res) == True and ifExists(res) == True:
            article = etree.SubElement(articles, "article")
            reference = etree.SubElement(article, "Reference")
            reference.text = "DBLP"
            titre = etree.SubElement(article,"Titre")
            titre.text = res['title']
            auteurs = etree.SubElement(article, "Auteurs")
            for auteur_art in res['authors'] :
                nom = etree.SubElement(auteurs, "Nom_Auteur")
                nom.text = auteur_art
            type_art = etree.SubElement(article,"Type") 
            type_art.text=res['type']
            url_art = etree.SubElement(article,"URL")
            url_art.text = res['url']
            f = open("result.xml", "r") 
            lines = f.readlines()
            f.close()
            taille = len(lines)
            lines[taille-1]=""
            fichier = open ("result.xml","w")
            fichier.writelines(lines)
            fichier.close()
            fichier = open("result.xml","a")
            fichier.write(etree.tostring(article, pretty_print=True))
            fichier.write("</articles>")
            fichier.close()
            fichier = open ("result.xml","a")
            fichier.write(etree.tostring(article, pretty_print=True))


    print("****************************** Les publication pour ", AUTHOR," ***************************")
    for res in get_publications_by_author(AUTHOR) :
        print("URL : " , res['url'])
        print("Auteurs :" ,res['authors'])
        print("Titre : " , res['title'])
        print("type : ", res['type'])
        print("**************************************************")
    
    #print(get_publications_by_author(AUTHOR))
    

if __name__ == "__main__":
    # execute only if run as a script
    main()
