# PJI - Projet 30

*Un outil pour l'analyse et la visualisation de collaborations scientifiques*

[Lien Sujet](https://www.fil.univ-lille1.fr/~salson/pji/projet.php?id=30)

# Récuparation du projet 

```
$ git clone https://github.com/mvkopp/pji-avennec-iguichi.git
```


# Objectifs

Développer une interface web qui permettrait à des chercheurs d ‘un même laboratoire d’avoir des suggestions de collaboration. 
Pour cela nous allons utiliser les informations des services tels que DBLP, HAL et Crossref. Il va également être possible d’identifier des interêts communs entre les différentes publications des chercheurs grâce aux mots clés. Ces mots clés seront trouvés grâce à du Top Modelling réalisé sur les différents articles.

- Construire un réseau social scientifique.
- Connecter les scientifiques qui se citent entre eux.
- Créer des connexions entre scientifiques ayant des intérêts communs.
- Possibilité d’élargir les domaines en cas de développement générique.

# Compte rendu

### **Semaine 1** - 23/03/20

Objectifs : 

- [x] Se familiariser avec le module python dblp 
- [x] Se familiariser avec l'API Crossref
- [x] Créer un programme qui va scraper le site [CRIStAL](https://www.cristal.univ-lille.fr/gt/optima) afin d'en récuperer les membres permanents
- [x] Créer un programme qui va à partir d'un nom de scientifique, trouver ses articles dans les bases de données tel que dblp, crossref
- [x] Se familiariser avec igraph
- [ ] Se familiariser avec Gephi (Faire le tuto)
- [x] Liste des différentes informations récupérés par DBLP (utiles et pas utiles), Crossref etc..
- [x] Choisir comment stocker les données qu’on peut déjà extraire
- [x] Réalisation d'un diagramme de gantt (Gestion de projet) 

> Questions ? 
> - Devons-nous récupérer les abstract des articles par scraping ? ou par utilisation d'une API ? (Articles sur différents sites)
> ***Pour l'instant pas de récupération des abstract, attendre de voir l'avancement du projet pour décider***

> Notes :
> - Utilisation du module [requests](https://pypi.org/project/requests/)

### **Semaine 2** - 30/03/20

Objectifs : 

- [x] Recupérer les données en quantité (tous les membres permanents de CRIStAL)
- [x] Connecter les résultats extraits de DBLP, Crossref
- [x] Mettre en place vérification que les personnes retournés sont les mêmes dans un site ou l’autre (second nom de famille etc)
- [ ] Mettre en place une fonction qui va chercher si les co-auteurs des membres permanents de l'équipe OPTIMA ont eux-mêmes des publications.
- [x] Récupérer tous les membres permanents et non permanent du site CRIStAL grâce au scraping
- [x] Remplacer les entités HTML par des caractères unicode
- [x] Créer fonction qui va calculer la précision du nom d'autheur donnée par l'utilisateur et des noms d'auteurs dans les articles récupérés

> Questions ?
> - Comment gérer les cas où il n'y a pas de titre dans les résultats (ex : site=Crossref, auteur=Laurent Noé, article=1) ?
> ***Si pas de titre, on ne considère pas l'article***


> Notes : 
> - Utilisation du module [Unidecode](https://pypi.org/project/Unidecode/)
> - Utilisation du module [HTML.unescape](https://docs.python.org/3/library/html.html#html.unescape) pour échapper les caractères spéciaux 
> - Utilisation du module os pour vérifier si un fichier est vide
> - Utilisation du module decimal

### **Semaine 3** - 06/04/20

Objectifs :

- [x] Mettre à jour diagramme de gantt 
- [x] Créer fichier graph en utilisant iGraph
- [x] Réaliser une importation sur Gephi
- [x] Réflechir à comment montrer les informations extraites de façon intuitive
- [x] Réaliser une exportation avec Gephi
- [x] Se documenter sur les algos de détections
- [ ] Appliquer les algos

Notes : /

### **Semaine 4** - 13/04/20

Objectifs : 

- [x] Commencer à mettre en place interface
- [x] Terminer les choses qui n'ont pas été terminés
- [x] Travailler de manière approfondi le rapport

Notes : /

### **Semaine 5** - 20/04/20

Objectifs : 

- [x] Ajout de fonctionnalité ou Debug
- [x] Finir le compte rendu du projet à 90% (**Rendu le 27/04/20**)

### **Semaine 6** - 27/04/20

Objectifs : 

- [x] Rendre le compte rendu du projet à 90% (**27/04/20**)
- [ ] Customiser l'interface
- [ ] Mettre en place les politesse des API

Notes : /

### **Semaine 7** - 4/05/20

- [ ] Créer tutoriel sur la façon d'utiliser l'application et ses fonctionnalités
- [ ] Créer un questionnaire de satisfaction/critique pour une première utilisation de l'application (ergonomie, utilité, etc..)
- [ ] Mettre en place l'analyse textuelle
- [ ] (Bonus) Analyse textuelle amélioré

# Structure du dossier

```
├── scrape_scientist.py         # Python file (Scrape OPTIMA members)
├── crossref_api.py             # Python file (Crossref API functions)
├── dblp_api.py                 # Python file (DBLP API functions)
├── articles_database.xml       # XML file (Articles database)
├── main.py                     # Python file (Program main function)
├── .gitignore                  # Gitignore file
└── README.md                   # Documentation du projet

```

# Link useful 

[Gantt Diagram](https://docs.google.com/spreadsheets/d/1AwLWuZqR6-Q6r1V8xphJ6M7TYemzvgg7aioNEova620/edit#gid=1115838130)

[DBLP API](https://dblp.uni-trier.de/faq/13501473)

[HAL API](http://api.archives-ouvertes.fr/ref/author)

[Crossref API](https://github.com/CrossRef/rest-api-doc)

# Authors 

**Mael AVENNEC** - [mael.avennec.etu@univ-lille.fr](https://github.com/mvkopp)

**Imad IGUICHI** - [imad.iguichi.etu@univ-lille.fr](https://gitlab-etu.fil.univ-lille1.fr/iguichi)