import requests
import unidecode
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

def scrape_webpage_cristal_all_groups_teams():
    """
    Scrape the CRIStAL webpage and recover all groups with their teams

    :params : /
    :returns: (dict) dictionnary of all CRIStAL groups

    :example:
    >>> scrape_webpage_cristal_all_groups_teams()
    {'MSV : Modélisation pour les Sciences du Vivant': ['biocomputing', 'bonsai'], 'CI2S : Conception Intégrée de Systèmes et Supervision': ['dicot', 'mocis', 'moses'], 'SEAS : Systèmes Embarqués Adaptatifs et Sécurisés': ['2xs', 'east', 'emeraude'], 'Image': ['3d-sam', 'fox', 'imagerie-couleur'], 'OPTIMA : OPTImisation : Modèles et Applications': ['bonus', 'inocs', 'orkad', 'osl'], 'DatInG : Data Intelligence Group': ['links', 'magnet', 'sigma', 'sequel'], 'GL : Génie Logiciel': ['caramel', 'carbon', 'rmod', 'spirals'], 'CO2 :  Control and scientific Computing': ['cfhp', 'defrost', 'shoc', 'valse'], 'I2C : Interaction et Intelligence Collective ': ['bci', 'loki', 'mint', 'noce', 'smac']}
    """
    URL = 'https://www.cristal.univ-lille.fr'
    
    teams={}

    page=requests.get(URL) # recover the url content
    soup = BeautifulSoup(page.content,'html.parser')

    res = soup.find(id='topMain')
    searchTab=res.find('li',{'class':'mega-menu-item'})

    rows = searchTab.find('ul').find('li').find('div').findAll('div',{'class':'row'}) # recover all rows
    for row in rows :
        columns=row.findAll('div',{'class':'col-md-3'})
        for column in columns :
            if(column.find('ul').find('li').find('a').find('span',{'class':'mega-menu-sub-title'}) != None):
                group = column.find('ul').find('li').find('a').find('span',{'class':'mega-menu-sub-title'}).text
                teams[group]=[]
                sections=column.find('ul').find('li').find('ul').findAll('li')
                for section in sections :
                    team=section.find('a').text # find the name
                    team=team.replace("\n","") # escape the line breaks
                    team=team.strip() # escape the spaces before and after the words
                    team=team.replace(" ","-") # replace space between word by a dash
                    team=team.lower() # transform the name to lower case
                    team=unidecode.unidecode(team)
                    teams[group].append(team) # add the team name to the result list
    return teams

def scrape_webpage_cristal_all_teams():
    """
    Recover all the teams

    :params : /
    :returns: (list) the list of all CRIStAL teams

    :example:
    >>> scrape_webpage_cristal_all_teams()
    ['biocomputing', 'bonsai', 'dicot', 'mocis', 'moses', '2xs', 'east', 'émeraude', '3dsam', 'fox', 'imageriecouleur', 'bonus', 'inocs', 'orkad', 'osl', 'links', 'magnet', 'sigma', 'sequel', 'caramel', 'carbon', 'rmod', 'spirals', 'cfhp', 'defrost', 'shoc', 'valse', 'bci', 'loki', 'mint', 'noce', 'smac']
    """
    all_groups_teams = scrape_webpage_cristal_all_groups_teams()
    teams=[]
    for key in all_groups_teams :
        teams+=all_groups_teams[key]
    return teams

def scrape_webpage_cristal_members_by_teams(team):
    """
    Scrape all the members of a team given

    :params: - team (str) the team name
    :returns: (dict) a dictionnary with the permanents and not permanents separate
    
    :example:
    >>> scrape_webpage_cristal_members_by_teams('bci')
    {'permanent': ['François Cabestaing', 'Marie-Hélène Bekaert', 'Claudine Botte-Lecocq', 'José Rouillard', 'Jean-Marc Vannobel'], 'non-permanent': ['Jimmy Petit', 'Camille Bordeau', 'Claire Dussard']}
    """
    URL='https://www.cristal.univ-lille.fr/equipes/'
    
    members={}
    members['permanent']=[]
    members['non-permanent']=[]

    page=requests.get(URL+team) # recover the url content
    soup = BeautifulSoup(page.content,'html.parser')
    
    res = soup.find(id='membres')        
    columns=res.find('div',{'class':'container'}).find('div',{'class':'row'}).findAll('div',{'class':'col-md-4'})
    for column in columns :
        
            groups = column.find('ul').findChildren('li',recursive=False)
            for group in groups :
                list_members=group.find('ul').findChildren('li',recursive=False)
                for list_member in list_members :
                    if(list_member.find('a') != None):
                        member=list_member.find('a').text
                    else:
                        member=list_member.text
                        member=member.replace("\n","") # remove the line break
                        member=member.strip() # remove spaces before and after the name
                        
                        
                    if (column.find('h3').text.lower().replace(" ","").replace("\n","") == 'permanents'):
                        members['permanent'].append(member)
                    else :
                        members['non-permanent'].append(member)
    return members
            

def recover_all_cristal_members():
    """
    Recover all cristal members

    :params: /
    :returns: (dict) a dictionnary with permanent members and not permanent members ordered separatly
    """
    members={}
    members['permanent']=[]
    members['non-permanent']=[]

    teams=scrape_webpage_cristal_all_teams()

    for team in teams:
        team_members=scrape_webpage_cristal_members_by_teams(team)

        members['permanent']+=team_members['permanent']
        members['non-permanent']+=team_members['non-permanent']

    return members

def recover_all_cristal_members_with_teams():
    """
    """
    all_members=dict()
    all_groups = scrape_webpage_cristal_all_groups_teams()
    for group in all_groups :
        for team in all_groups[group] :
            team_members=scrape_webpage_cristal_members_by_teams(team)
            for member in team_members['permanent'] :
                all_members[member]=group
            for member in team_members['non-permanent'] :
                all_members[member]=group
    return all_members

def main():
    """
    main function
    """
    #URL="https://www.cristal.univ-lille.fr/gt/optima/"
    #scrape_webpage_cristal_optima(URL)

    print(len(recover_all_cristal_members()['non-permanent']))
    

if __name__ == "__main__":
    # execute only if run as a script
    main()
