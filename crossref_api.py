import requests
from lxml import etree
import xml.etree.cElementTree as ET


def get_articles_by_author(author):
    """
    GET informations about all articles where the auhtor is involved

    :params : - author (str) the author name
    :returns: (list) list of all articles where the author is involved

    """
    res=[]
    GET_URL="https://api.crossref.org/works"
    response=requests.get(GET_URL+'?query.author='+author)
    response=response.json()

    items=response['message']['items']

    i=0

    for item in items:
        tmp={}
        # publisher
        publisher=item['publisher']
        tmp['publisher']=publisher
        # type
        document_type=item['type']
        tmp['type']=document_type
        # title
        title=item['title'][0]
        tmp['title']=title
        # authors
        authors=[]
        for author in item['author']:
            author_name=author['given']+' '+author['family']
            authors.append(author_name)
        tmp['authors']=authors
        # abstract
        if 'abstract' in item :
            abstract = item['abstract']
            tmp['abstract']=abstract
        # url  
        url=item['URL']
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
    for res in get_articles_by_author(AUTHOR):
        if test_auteur_by_name(AUTHOR,res) == True and ifExists(res) == False:
            article = etree.SubElement(articles, "article")
            reference = etree.SubElement(article, "Reference")
            reference.text = "Crossref"
            titre = etree.SubElement(article,"Titre")
            titre.text = res['title']
            publier_par = etree.SubElement(article,"Publisher")
            publier_par.text = res['publisher']
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


    print("****************************** Les publication pour ", AUTHOR," ***************************")
    for res in get_articles_by_author(AUTHOR) :
        print("URL : " , res['url'])
        print("Publie par : " , res['publisher'])
        print("Auteurs :" ,res['authors'])
        print("Titre : " , res['title'])
        print("type : ", res['type'])
        print("**************************************************")
    
    print len(get_articles_by_author(AUTHOR))
    #print(get_articles_by_author(AUTHOR))
    

if __name__ == "__main__":
    # execute only if run as a script
    main()
