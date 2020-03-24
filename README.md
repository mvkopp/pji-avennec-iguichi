# pji-avennec-iguichi

PJI [Project 30](https://www.fil.univ-lille1.fr/~salson/pji/projet.php?id=30) "Un outil pour l'analyse et la visualisation de collaborations scientifiques"



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

Questions ? 

- Devons-nous récupérer les abstract des articles par scraping ? ou par utilisation d'une API ? (Articles sur différents sites)

Notes :
- Utilisation du module [requests](https://pypi.org/project/requests/)

### **Semaine 2** - 30/03/20

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