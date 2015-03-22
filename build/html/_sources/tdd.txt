########################################
Développement dirigé par les tests
########################################

Le développement dirigé par les tests, grossièrement traduit de l'anglais Test 
Driven Development, est une technique de développement utilisée par beaucoup de 
programmeurs.

En effet, c'est grâce à cette technique que l'on peut le mieux s'assurer de la 
fonctionnalité du site et de la simplicité du code. Dans un travail de longue 
haleine, cette méthode devient nécessaire pour ne pas être redondant dans son 
code et pour le rendre le plus clair possible.

Dans cette première partie, nous allons nous intéresser au côté théorique de ce
type de développement avant de se lancer dans un réel projet.

Le développement dirigé par les tests est composé de deux tests importants et
bien différents.

Les tests fonctionnels
=======================

Le test fonctionnel, comme son nom l'indique, cherche à tester la fonctionnalité
du site. Plus précisément, il se met du côté de l'utilisateur du site. Il va par
exemple vérifier que les titres et les textes apparaissent, mais il va aussi 
regarder si les différents boutons ou champs de textes fonctionnent.
    
Voici un exemple de test fonctionnel:

**Mettre un test fonctionnel plus tard**

Nous pouvons déjà voir que les commentaires sont énormément présents dans ce
test. En effet, la convention est que l'on crée un scénario pour expliquer 
exactement ce que l'on teste. Dans cet exemple, nous avons le professeur
Jean-Paul qui entend parler d'un site pour apprendre les mathématiques où il y a
un dashboard qui lui permet de gérer son travail. Il va donc essayer
tous les boutons et toutes les fonctionnalités.

Les tests unitaires
====================

Le test unitaire, lui, se base plus sur le point de vue du programmateur. Si on 
pouvait considérer le test fonctionnel comme un test externe, le test unitaire,
lui, serait le test interne. Ce qu'il teste ne sera jamais vu, car il permet de 
vérifier que le code fonctionne comme prévu.

Voici un exemple:

**Test unitaire** A rajouter un jour

Le cycle du développement dirigé par les tests
===============================================

Quand on veut programmer à l'aide du développement dirigé par les tests, on 
tente de suivre un certain cycle:

1.  Tout d'abord, il est **impératif** d'écrire un test avant même d'écrire
    n'importe quelle ligne de code. En effet, l'idée du Test Driven Development
    est d'être sûr qu'un test échoue avant d'écrire notre code. Le test peut
    être fonctionnel ou unitaire, cela dépendant de la partie de votre
    application que l'on souhaite développer. Le test va évidemment retourner
    un message négatif, mais c'est normal étant donné que rien n'a été codé
    concernant la fonctionnalité testée.
    
2.  Ensuite seulement, le but est d'écrire un minimum de code possible
    pour que le test précédemment lancé fonctionne. Il faut donc réussir
    à ce que le test, une fois relancé, retourne un résultat positif. Il faut
    faire attention à ne pas développer une fonctionnalité qui n'est pas dans
    le test
    
3.  Une fois le code écrit, on peut relancer ce test. Si le résultat
    est positif, on peut passer à l'étape suivante. Dans le cas contraire,
    il faudra refaire les étapes 2 et 3 jusqu'à ce que le test fonctionne.
    
4.  Finalement, il ne reste qu'à restructurer le code précédemment écrit pour
    qu'il soit plus lisible. Il faut faire très attention durant cette étape à
    ne rien ajouter ou enlever. Le code doit garder le même résultat.
    
Une fois que ces 4 étapes ont été effectuées, il ne reste qu'à
recommencer avec une autre fonctionnalité de l'application, jusqu'à
que celle-ci soit finie.

..  figure:: images/TDD.png
    :width: 50%
    :align: center
    
    Schéma résumant les 4 étapes du Développement dirigé par les tests

Gain de temps?
===============

En lisant ces 4 étapes répétitives, on ne peut que se demander si le Test
Driven Development et son cycle compliqué est réellement un atout et un gain
de temps pour le programmeur.

Il est clair que, sur un travail de petite taille, tout coder n'aurait pas
énormément de sens, car tout peut être facilement essayable par soi-même.
Dans le cas d'un travail d'une certaine consistance, ce n'est pas pareil.
C'est uniquement en testant que l'on peut être sûr de son code, car cela
signifie qu'il est valide et devrait le rester.