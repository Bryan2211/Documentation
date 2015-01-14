#################################
Documentation
#################################

Différentes technologies
==========================

Pour créer mon application ( dashboard professeur ), j'ai fait recourt aux
technologies suivantes.

HTML5 (Hypertext Markup Language)
**********************************

HTML est la base de toute page web. En effet, c'est ce qui nous permet
d'afficher du texte, des images. Il est principalement utilisé avec CSS (pour la
mise en page) et JavaScript (pour l'interactivité des pages).

J'ai utilisé HTML5 pour faire le frontal ( plus connu sous le nom front-end ). 
Le frontal correspond à ce que l'utilisateur voit. Il est opposé au back-end,
qui est la partie qui travaille derrière mais que l'utilisateur ne voit pas.

CSS3 (Cascading Style Sheets)
*******************************

CSS3 a été utilisé pour mettre en page mon code HTML. Cela a donc aussi
contribué à la partie front-end de mon application. C'est CSS qui permet de
modifier la police du texte, modifier la taille des images, ou encore
de modifier la couleur du font. CSS permet donc de rendre une page potable
pour l'oeil.
    
Bootstrap
***********

Bootstrap est un framework qui contient du code HTML et CSS. J'ai utilisé
Bootstrap comme base pour mon dashboard en utilisant le modèle *Charisma* 
[#f1]_. L'avantage de Bootstrap est qu'il offre des
design adaptatifs, qui signifie que la mise en page va s'adapter à la taille de
l'écran.

Voici un exemple d'adaptation:

.. image:: source/images/fullscreen.png

Voici à quoi ressemble le dashboard sur un écran d'ordinateur.

.. image:: source/images/smallscreen.png

Et voici ce que la page devient si l'on zoome ou si l'on réduit la taille de la
fenêtre.
    
Django
*******

Django est un framework spécialisé dans Python. C'est un des framework les plus
utilisés. Nous avons choisi Django pour le projet car, travaillant sous Python,
il est le plus documenté et le plus connu.

Grâce à Django, nous avons pu gérer des classes et des héritages, des vues et
des urls.

Application au projet
======================

Dans le projet final, qui, rappelons-le, consistera en un site d'e-learning pour
les mathématiques, ma partie pratique sera le dashboard professeur, donc
l'endroit ou les professeurs pourront gérer leurs exercices, leurs classes et
leurs élèves. La raison pour laquelle cette partie du site est si importante
est que sans un dashboard parfaitement opérationnel, il deviendrait chaotique
pour les professeurs de gérer leurs différentes responsabilités.

Toutes les fonctionnalités ayant déjà été expliquées auparavant, je ne vais pas
repasser dessus.

Wireframes, ou "scénarios du site"
===================================

Modèles et diagrammes UML
==========================

Modèles User
**************

Les modèles User, c'est-à-dire les modèles qui héritent du modèle Django de base
User, sont les plus importants dans la conception de mon dashboard. En effet, il
y a tout d'abord Student, dont les propriétés sont le nom, le prénom et le
niveau. Ce sont donc les caractéristiques de base d'un utilisateur qui doit
apprendre.

De ce modèle Student hérite une classe Teachers, qui est évidemment le point
central de notre travail. Etant donné qu'il hérite de Students, il possède
les mêmes propriétés qu'un élève. Je ne trouve pas nécessaire d'ajouter une
caractéristique, bien qu'on puisse par exemple ajouter la branche qu'il
enseigne, même si cela peut paraître superflu sur un site pour apprendre
les mathématiques.

Grâce à ces utilisateurs, nous pouvons créer des classes ou groupes, avec le
modèle Group. Celui-ci possède un nom, un ou plusieurs élèves ou professeurs et
des exercices assignés en devoir.

Modèles d'exercices ou de cours
********************************

M'occupant du professeur, je dois aussi pouvoir gérer les exercices, chapitres,
QCM ou cours qu'il voudra ajouter sur le site.

Partons tout d'abord du modèle Theme, qui possède la propriété name. Grâce à
cette caractéristique nous pouvons définir la classe Chapter. En effet, quand un
professeur crée un chapitre, il devrait pouvoir choisir un thème, mais aussi un
nom, ce qui explique l'entrée name.

A ces chapitres peuvent être associés des exercices, c'est pourquoi il y a le
modèle Exercise, où il est décrit les utilisateurs, le propriétaire, les
chapitres dans lequel il appartient, quand il a été écrit ou mis-à-jour,
son niveau, des indices et des commentaires. Ce modèle est le centre de toutes
les classes concernant les exercices.

Diagramme UML
***************

Implémentation avec le reste du projet
=======================================

.. rubric:: Note de bas de page

..  [#f1] http://usman.it/free-responsive-admin-template/