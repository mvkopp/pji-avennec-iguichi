import requests
from lxml import etree
import sys


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


def main():
    """
    main function
    """
    AUTHOR='laetitia jourdan'

    articles = etree.Element("Articles")

    for res in get_publications_by_author(AUTHOR) :
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
    fichier = open ("result.xml","a")        
    fichier.write(etree.tostring(articles, pretty_print=True))

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
