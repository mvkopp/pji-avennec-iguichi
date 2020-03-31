# Compte rendu Projet 30
Autheur : Mael AVENNEC et Imad IGUICHI

# Informations récupérés par les API

## DBLP

Format JSON : 

result : 
- hits : 
    - @total : (str) nombre de résultat trouvé

    - @sent : (str) nombre de résultat reçu dans la reqûete

    - hit : (array) tableau de tous les résultats de la requête
        - @id : (str) id de la publication
        - info : 
            - authors :
                - author : (array) tableau contenant les auteurs de la publications
                    - @pid : (str) id de l'auteur
                    - text : (str) nom de l'auteur

## CROSSREF

## HAL