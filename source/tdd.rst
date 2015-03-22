########################################
Développement dirigé par les tests
########################################

Le développement dirigé par les tests, grossièrement traduit de l'anglais Test 
Driven Development, est une technique de programmation utilisée par beaucoup de 
programmeurs.

En effet, c'est grâce à cette technique que l'on peut le mieux s'assurer de la 
fonctionnalité du site et de la simplicité du code. Dans un travail de longue 
haleine, cette méthode devient nécessaire pour ne pas être redondant dans son 
code et pour le rendre le plus clair possible.

Dans cette première partie, nous allons nous intéresser au côté théorique de ce
type de programmation avant de se lancer dans un réel projet.

Le développement dirigé par les tests est composé de deux tests importants et
bien différents.

Le test fonctionnel
=====================

Le test fonctionnel, comme son nom l'indique, cherche à tester la fonctionnalité
du site. Plus précisément, il se met du côté de l'utilisateur du site. Il va par
exemple vérifier que les titres et les textes apparaissent, mais il va aussi 
regarder si les différents boutons ou champs de textes marchent.
    
Voici un exemple de test fonctionnel:

**Mettre un test fonctionnel plus tard**

Nous pouvons déjà voir que les commentaires sont énormément présents dans ce
test. En effet, la convention est que l'on crée un scénario pour expliquer 
exactement ce que l'on teste. Dans cet exemple, nous avons le professeur
Jean-Paul qui entend parler d'un site pour apprendre les mathématiques où il y a
un dashboard qui lui permet de gérer son travail. Il va donc essayer
tous les boutons et toutes les fonctionnalités.

Evidemment, cela peut paraître obsolète, mais ça vous aide à vous y retrouver.

Le test unitaire
=================

Le test unitaire, lui, se base plus sur le point de vue du programmateur. Si on 
aurait pu considérer le test fonctionnel comme un test externe, le test unitaire
lui serait le test interne. Ce qu'il test ne sera jamais vu, car il permet de 
vérifier que le code est le plus propre et le plus simple possible.

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
    application que vous souhaitez développer. Vous allez évidemment recevoir
    un message disant que votre test a échoué, mais c'est normal étant
    donné que vous n'avez rien codé. Cela consiste donc à essayer un
    programme encore non-existant.
    
2.  Ensuite seulement, le but est d'écrire un minimum de code possible
    pour que le test précédemment lancé fonctionne. Il faut seulement s'occuper
    de ce que le test cherchait à essayer, pas plus, pas moins.
    
3.  Une fois que vous pensez avoir accompli ce que le test de la première étape
    vous disait avoir raté, vous pouvez relancer ce test. Si le résultat
    est positif, vous pouvez passer à l'étape suivante. Dans le cas contraire,
    il va vous falloir refaire l'étape 2 et 3 jusqu'à ce que le test soit
    positif.
    
4.  L'étape finale: il va falloir réécrire et réstructurer le code précédent
    histoire qu'il soit plus agréable à l'oeil et le rendre plus lisible.
    Il faut faire très attention durant cette étape à ne rien rajouter ou
    enlever. Le code doit garder le même résultat.
    
Une fois que ces 4 étapes ont été effectuées, il ne reste évidemment qu'à
recommencer avec une autre fonctionnalité de l'application, jusqu'à
que celle-ci soit finie.

..  figure:: images/TDD.jpg
    :width: 70%
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
signifie que notre code est valide, et devrait le rester.


    

    


    



