#################################
Documentation
#################################

Modèles
========

Modèles utilisés
******************

..  literalinclude:: code/models.py
    :language: python
    :linenos:

Il y a tout d'abord notre classe Teacher, qui constitue bien évidemment le
point central de notre application. La classe Teacher possède les propriétés
suivantes: prénom, nom, adresse e-mail et l'école dans laquelle il enseigne.
Il n'y a pas réellement d'autres propriétés à lui rajouter.

Pour qu'il y ait des professeurs, il faut aussi des élèves, c'est pourquoi
j'ai une classe dénommée Student. Les propriétés ressemblent beaucoup à celles
de Teacher étant donné que les deux classes correspondent à des classes
d'utilisateur. Ces propriétés sont: prénom, nom, adresse e-mail, école et
compétences de l'élève, établies par rapport à certains thèmes accomplis.

Finalement, ces deux classes sont réunies dans une classe nommée Group, qui
pourrait s'apparenter à une classe d'école. En effet, la classe Group possède
1 à plusieurs professeurs, 1 à plusieurs élèves, un nom, des devoirs, des
taux de réussites par rapport aux exercices réalisés en général, et une date
de création.

Diagramme UML
***************




Implémentation avec le reste du projet
=======================================

Comme déjà expliqué, ma partie, le dashboard professeur, servira de lieu de
référence pour le professeur qui utiliserait le site. En effet, c'est seulement
depuis cette partie qu'il pourra gérer tout ce qui le concerne.

Certaines fonctionnalités, tel que la création d'exercices ou de chapitres,
feront appel aux applications de mes compagnons. En effet, le bouton devra aller
chercher les formulaires correspondant.

Les problèmes que nous pourrions rencontrer lors de la mise en commun de nos
différentes applications seraient des conflits, mais qui pourraient facilement
être gérables si on y fait attention en cherchant les erreurs.

.. rubric:: Note de bas de page

..  [#f1] http://usman.it/free-responsive-admin-template/