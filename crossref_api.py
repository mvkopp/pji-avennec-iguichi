import requests

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


def main():
    """
    main function
    """
    AUTHOR='laetitia vermeulen jourdan'
    print("****************************** Les publication pour ", AUTHOR," ***************************")
    for res in get_articles_by_author(AUTHOR) :
        print("URL : " , res['url'])
        print("Publie par : " , res['publisher'])
        print("Auteurs :" ,res['authors'])
        print("Titre : " , res['title'])
        print("type : ", res['type'])
        print("**************************************************")
    
    #print(get_articles_by_author(AUTHOR))
    

if __name__ == "__main__":
    # execute only if run as a script
    main()
