#####################################################################################
Conception du dashboard professeur à l’aide du développement dirigé par les tests
#####################################################################################

Introduction
=============

Dans ce travail, je vais tout d'abord documenter mon travail pratique. Ce
travail consiste en la conception d'un dashboard pour les professeurs
utilisant le framework Django tout en essayant de programmer
avec le développement dirigé par les tests. 
Ce dashboard fera partie d'un projet plus grand: un site d'e-learning pour les
mathématiques.
Tous les termes spécifiques tels que framework seront expliqués par la suite.

Cette documentation parlera tout d'abord de l'intérêt de ce travail pratique.
Il y aura aussi le wireframe du dashboard et un diagramme UML expliquant mes
différents modèles Django. J'expliquerai par la suite comment j'ai utilisé
les différentes technologies pour créer mon application et comment
je pourrai l'intégrer au projet final (le site) en essayant de souligner les
difficultés que je pourrai rencontrer pendant l'intégration.

Par la suite, j'essaierai de résumer les connaissances de bases relatives
au développement dirigé par les tests. Ceci consistera à expliquer les
différents termes et à surtout à expliquer comment cela fonctionne et quels
sont les avantages.

Finalement, j'expliquerai comment créer une ébauche de dashboard (créer un
dashboard complet étant trop long et trop compliqué à tester de par le nombre
important de boutons et de fonctionnalités) en utilisant ce fameux
développement dirigé par les tests

Explications des termes spécifiques
====================================

Pour être sûr que tout le monde comprenne de quoi nous allons parler,
il va nous falloir expliquer le lexique spécifique à nos deux sujets:
dashboard professeur et développement dirigé par les tests.

Framework
**********

Un **framework**, ou **structure logicielle**, sert de base à un programme.
En effet, c'est de par ses structures de base que l'on peut le plus facilement
programmer. C'est donc une grande aide à tout informaticien. Les framework les
plus connus seraient, par exemple, Django, Bootstrap ou Ruby On Rails.

Il est important de noter que les frameworks sont souvent spécialisés dans un
langage informatique très précis. Par exemple, Django utilise Python, Bootstrap
utilise HTML et CSS et Ruby on Rails utilise Ruby.

Un framework est en autre très utile pour la programmation orientée objet. Ce
type de programmation permet d'établir des liens entre les différents objets.
Le framework aide à créer des classes et surtout des héritages. 

Classes et héritages
*********************

Les classes correspondent à un moule dans lequel on met différentes
informations pour créer un objet. Par exemple, pour une voiture, on pourrait
définir sa couleur, sa marque ou encore son age. Tout ce qu'il reste à faire
est de donner des valeurs à ces trois propriétés pour "créer" la voiture.

Le concept d'héritage n'est pas beaucoup plus compliqué. En effet, un héritage
consiste à créer une classe en prenant comme base les caractéristiques d'une 
autre, ce qui nous permet d'en rajouter d'autre. Dans un cas qui nous
intéresserait plus, un élève possède comme spécificités un nom, un prénom et
une école. On peut grâce à ça créer une classe Professeur, qui aura les
mêmes caractéristiques mais à laquelle on pourrait ajouter la branche qu'il
enseigne.

Diagramme UML
**************

Quand l'on possède de nombreuses classes, il devient indispensable de pouvoir
voir rapidement quelles relations ces classes entreprennent entre elles. Pour
ceci, le meilleur moyen de le faire est de créer un diagramme UML. Un diagramme
schématise les objets et indique leurs différentes relations (relation simple
avec une clé étrangère ou aussi plusieurs-à-plusieurs (ManyToMany)).

Il existe de nombreux programmes permettant de réaliser des diagrammes UML
clairs et présentables, comme boUML, argoUML ou Poseidon.

Wireframe
**********

Un **wireframe** est un schéma consistant à mettre en valeur les relations entre les
différentes pages d'un site web. Cela explique par exemple ce qu'il se passe si 
l'on clique sur tel ou tel bouton. Cela consiste donc à pouvoir voir ou
exactement l'on peut aller en manipulant les fonctionnalités du site.