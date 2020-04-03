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

def scrape_webpage_cristal_all_teams():
    """
    Scrape the CRIStAL webpage and recover all the teams

    :params : /
    :returns: (list) the list of all CRIStAL teams

    :example:
    >>> scrape_webpage_cristal_all_teams()
    ['biocomputing', 'bonsai', 'dicot', 'mocis', 'moses', '2xs', 'east', 'émeraude', '3dsam', 'fox', 'imageriecouleur', 'bonus', 'inocs', 'orkad', 'osl', 'links', 'magnet', 'sigma', 'sequel', 'caramel', 'carbon', 'rmod', 'spirals', 'cfhp', 'defrost', 'shoc', 'valse', 'bci', 'loki', 'mint', 'noce', 'smac']
    
    """
    URL = 'https://www.cristal.univ-lille.fr'
    
    teams=[]

    page=requests.get(URL) # recover the url content
    soup = BeautifulSoup(page.content,'html.parser')

    res = soup.find(id='topMain')
    searchTab=res.find('li',{'class':'mega-menu-item'})

    rows = searchTab.find('ul').find('li').find('div').findAll('div',{'class':'row'}) # recover all rows
    for row in rows :
        columns=row.findAll('div',{'class':'col-md-3'})
        for column in columns :
            if(column.find('ul').find('li').find('a').find('span',{'class':'mega-menu-sub-title'}) != None):   
                sections=column.find('ul').find('li').find('ul').findAll('li')
                for section in sections :
                    team=section.find('a').text # find the name
                    team=team.replace(" ","") # escape the spaces
                    team=team.replace("\n","") # escape the line breaks
                    team=team.lower() # transform the name to lower case
                    teams.append(team) # add the team name to the result list

    return teams
            
    
            

def main():
    """
    main function
    """
    #URL="https://www.cristal.univ-lille.fr/gt/optima/"
    #scrape_webpage_cristal_optima(URL)

    print(scrape_webpage_cristal_all_teams())
    

if __name__ == "__main__":
    # execute only if run as a script
    main()
