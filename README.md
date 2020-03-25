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
- [x] Créer un programme qui va scraper le site [CRIStAL](www.cristal.univ-lille.fr/gt/optima) afin d'en récuperer les membres permanents
- [x] Créer un programme qui va à partir d'un nom de scientifique, trouver ses articles dans les bases de données tel que dblp, crossref
- [x] Se familiariser avec igraph
- [ ] Se familiariser avec Gephi (Faire le tuto)
- [ ] Liste des différentes informations récupéré par DBLP (utiles et pas utiles), Crossref etc..
- [ ] Choisir comment stocker les données qu’on peut déjà extraire

Questions ? 

- Devons-nous récupérer les abstract des articles par scraping ? ou par utilisation d'une API ? (Articles sur différents sites)
-> ***Pour l'instant pas de récupération des abstract, attendre de voir l'avancement du projet pour décider***

Notes :
- Utilisation du module [requests](https://pypi.org/project/requests/)

### **Semaine 2** - 30/03/20

Objectifs : 

- [ ] Recupérer les données en quantité
- [ ] Connecter les résultats extraits de DBLP, Crossref, HAL ensemble
- [ ] Mettre en place vérification que les personnes retournés sont les mêmes dans un site ou l’autre (second nom de famille etc)
- [ ] Mettre en place une fonction qui va chercher si les co-auteurs des membres permanents de l'équipe OPTIMA ont eux-mêmes des publications.

Notes : /

### **Semaine 3** - 06/04/20

Objectifs : 

- [ ] Réflechir à comment montrer les informations extraites de façon intuitive
- [ ] Commencer à mettre en place interface
- [ ] Tester l'exportation avec Gephi
- [ ] Customiser l'interface
- [ ] Se documenter sur les algos de détections et expliquer dans le rapport
- [ ] Appliquer les algos

Notes : /

### **Semaine 4** - 13/04/20

Objectifs : 

- [ ] Terminer les choses qui n'ont pas été terminés
- [ ] Travailler de manière approfondi le rapport
- [ ] Créer tutoriel sur la façon d'utiliser l'application et ses fonctionnalités
- [ ] Créer un questionnaire de satisfaction/critique pour une première utilisation de l'application (ergonomie, utilité, etc..)
- [ ] Mettre en place l'analyse textuelle
- [ ] (Bonus) Analyse textuelle amélioré

Notes : /

### **Semaine 5** - 20/04/20

Objectifs : 

- [ ] Ajout de fonctionnalité ou Debug
- [ ] Finir le compte rendu du projet à 90% (**Rendu le 27/04/20**)

### **Semaine 6** - 27/04/20

Objectifs : 

- [ ] Rendre le compte rendu du projet à 90% (**27/04/20**)

Notes : /

### **Semaine 7** - 4/05/20

- A définir

# Structure du dossier

```
├── scrape_scientist.py         # Python file (Scrape OPTIMA members)
├── crossref_api.py             # Python file (Crossref API functions)
├── dblp_api.py                 # Python file (DBLP API functions)
└── README.md                   # Documentation du projet
```

# Link useful 

[DBLP API](https://dblp.uni-trier.de/faq/13501473)

[HAL API](http://api.archives-ouvertes.fr/ref/author)

[Crossref API](https://github.com/CrossRef/rest-api-doc)

# Authors 

**Mael AVENNEC** - [mael.avennec.etu@univ-lille.fr](https://github.com/mvkopp)

**Imad IGUICHI** - [imad.iguichi.etu@univ-lille.fr](https://gitlab-etu.fil.univ-lille1.fr/iguichi)