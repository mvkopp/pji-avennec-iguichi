import requests
from lxml import etree
from decimal import Decimal

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

def test_auteur_by_name(author):
    identique = 0 
    res = get_articles_by_author(author)
    for result in res :
        for auteur in result['authors']:
            if (auteur == author):
                identique = identique +1  
    nonIdentique = len(res) - identique       
    print(" ********************* Crossref :")
    print(identique ,"articles sont de meme auteur et ",nonIdentique,"articles sont pas de meme auteur")
    print(" Taux d'erreur pour = ", Decimal(nonIdentique) / Decimal(len(res)) *100,"%")
    identique = 0 
    nonIdentique = 0 
    res = get_publications_by_author(author)
    for result in res :
        for auteur in result['authors']:
            if (auteur == author):
                identique = identique +1  
    nonIdentique = len(res) - identique             
    print(" ********************* DBLP :")
    print(identique ,"articles sont de meme auteur et ",len(res)-identique,"articles sont pas de meme auteur")
    print(" Taux d'erreur pour = ",Decimal(nonIdentique) / Decimal(len(res)) *100,"%")

def main():
    """
    main function
    """
    #AUTHOR='Faiza Ajmi'
    AUTHOR='Olivier Nicol'
    print("****************************** Les publication pour ", AUTHOR," ***************************")
    for res in get_publications_by_author(AUTHOR) :
        print("URL : " , res['url'])
        #print("Publie par : " , res['publisher'])
        print("Auteurs :" ,res['authors'])
        print("Titre : " , res['title'])
        print("type : ", res['type'])
        print("**************************************************")
    
    print("*********************************************")
    test_auteur_by_name(AUTHOR)

    
    

if __name__ == "__main__":
    # execute only if run as a script
    main()
