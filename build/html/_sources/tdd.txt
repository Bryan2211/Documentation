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

Dans cette partie, nous allons nous intéresser au côté théorique de ce
type de développement.

Le développement dirigé par les tests est composé de deux tests importants et
bien différents, même s'il existe un troisième qui est utilisé dans un
context très précis.

Les tests fonctionnels
=======================

Le test fonctionnel, comme son nom l'indique, cherche à tester la fonctionnalité
du site. Plus précisément, il se met du côté de l'utilisateur du site. Il va par
exemple vérifier que les titres et les textes apparaissent, mais il va aussi 
regarder si les différents boutons ou champs de textes fonctionnent [#f4]_.

En général, on remplit ces tests de commentaires qui raccontent une histoire
pour pouvoir s'y retrouver plus facilement quand on le lit. Par exemple,
on pourrait racconter l'histoire d'un professeur qui découvre un site web
d'e-learning pour les mathématiques et qui d'abord crée un compte, puis
essaie de créer une classe.

Les tests unitaires
====================

Le test unitaire, lui, se base plus sur le point de vue du programmeur. Si on 
pouvait considérer le test fonctionnel comme un test externe, le test unitaire,
lui, serait le test interne. Ce qu'il teste ne sera jamais vu, car il permet de 
vérifier que le code fonctionne comme prévu [#f4]_.

Les tests d'approbation
========================

Plus rare, il existe aussi le test d'approbation qui peut même amener à un
développement plus précis: Acceptance Test Driven Development (ATDD), ou
développement dirigé par les tests d'approbation [#f5]_.

Le grand avantage de ces tests est qu'ils permettent un meilleur travail de
groupe. En effet, l'équipe travaillant sur le projet se réunit et décide des
critères de base de ce projet qui seront ensuite écrit en test. Par conséquent,
toute l'équipe est d'accord sur ces critères et il sera ensuite facile de voir
s'ils sont respectés.

Le cycle du développement dirigé par les tests
===============================================

Quand on veut programmer à l'aide du développement dirigé par les tests, on 
tente de suivre un certain cycle [#f4]_:

1.  Tout d'abord, il est **impératif** d'écrire un test avant même d'écrire
    n'importe quelle ligne de code. En effet, l'idée du développement dirigé par
    les tests est d'être sûr qu'un test échoue avant d'écrire notre code. Le
    test peut être fonctionnel, unitaire, ou d'approbation (dans le cadre du
    ATDD), cela dépendant de la partie de l'application que l'on souhaite
    développer. Le test va évidemment retourner un message négatif, mais c'est
    normal étant donné que rien n'a été codé concernant la fonctionnalité
    testée.
    
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
    :width: 70%
    :align: center
    
    Schéma résumant les 4 étapes du développement dirigé par les tests

Gain de temps?
===============

En lisant ces 4 étapes répétitives, on ne peut que se demander si le Test
Driven Development et son cycle compliqué est réellement un atout et un gain
de temps pour le programmeur.

Il est clair que, sur un travail de petite taille, tout tester n'aurait pas
énormément de sens, car tout peut être facilement essayable par soi-même.
Dans le cas d'un travail d'une certaine consistance, ce n'est pas pareil.
C'est uniquement en testant que l'on peut être sûr de son code, car cela
signifie qu'il est valide et devrait le rester.

.. rubric:: Note de bas de page

..  [#f4] PERCIVAL, Harry J.W., «Test Driven Development With Python», publié
    le 19 juin 2014

..  [#f5] «Acceptance Test Driven Development (ATDD): An Overview»,
    consulté le 25.03.2015,
    http://testobsessed.com/2008/12/acceptance-test-driven-development-atdd-an-
    overview/