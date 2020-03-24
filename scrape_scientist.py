import requests
from bs4 import BeautifulSoup

def scrape_webpage_cristal_optima(url):
    """
    Scrape the webpage of OPTIMA team of CRIStAL industry.

    :params: - url (str) the url webpage
    :returns: (list) the list of OPTIMA permanent members

    :example:
    >>> scrape_webpage_cristal_optima("https://www.cristal.univ-lille.fr/gt/optima/")
    ['Clarisse Dhaenens', 'Slim Hammadi', 'Laetitia Jourdan', 'Nouredine Melab', 'Frédéric Semet', 'El-Ghazali Talbi', 'Luce Brotcorne', 'Omar Abdelkafi', "Thomas Bourdeaud'Huy", 'Hervé Camus', 'Diego Cattaruzza', 'Bilel Derbel', 'Abdelkader El Kamel', 'Marie-Eléonore Kessaci', 'Arnaud Liefooghe', 'Khaled Mesghouni', 'Maxime Ogier', 'Benoît Trouillet', 'Nadarajen Veerapen']
    """
    members=[]
    
    page=requests.get(url) # recover the url content
    soup = BeautifulSoup(page.content,'html.parser')
    
    res = soup.find(id='membres') # all members of OPTIMA team
    types = res.find('ul') # first ul is Permanent members
    lists_scientists = types.findAll('ul') # recover all sub-category of permanent members

    for list_scientist in lists_scientists :

        scientists = list_scientist.findAll('li') # recover the member element

        for scientist in scientists :
            name_scientist = scientist.find('a').text
            members.append(name_scientist)

    return members
            

def main():
    """
    main function
    """
    URL="https://www.cristal.univ-lille.fr/gt/optima/"
    scrape_webpage_cristal_optima(URL)
    

if __name__ == "__main__":
    # execute only if run as a script
    main()
