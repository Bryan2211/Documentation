#############################
Fonctionnalités du dashboard
#############################

Ajouter un groupe
===================

La fonctionnalité de base de ce dashboard est la création de groupe. En créant
un groupe, le professeur sera par la suite capable de le gérer en gérant les
membres qui s'y trouvent mais aussi en y assignant des devoirs.

Pour créer un groupe, il suffit de se rendre sur Nouveau groupe, tout en bas
dans le menu de gauche. Cette action fera apparaître le formulaire de création
de groupe.

..  figure:: images/Newclass.jpg
    :width: 60%
    :align: center
    
    Formulaire de création de groupe
    
La seule exigence présente lors de la création d'un groupe est le nom. Une fois
le groupe créé, l'utilisateur actuel est automatiquement défini en tant que
professeur pour le groupe.

Le groupe précédemment créé sera désormais affiché en permanence dans le menu
de gauche du professeur, ce qui lui permet d'accéder à ses informations.


Gérer un groupe
================

Gérer les membres du groupe
***********************************

Depuis cette page, le professeur peut gérer les membres qui sont actuellement
enregistrés dans le groupe.

Il peut tout d'abord rajouter les élèves ou professeurs qu'il souhaite en
entrant leur nom d'utilisateur dans le champ à disposition.

..  figure:: images/class.jpg
    :width: 60%
    :align: center
    
    Page d'administration d'un groupe
    
Si le nom d'utilisateur rentré correspond bien à un étudiant ou à un professeur,
cet utilisateur sera rajouté dans la liste des membres.

..  figure:: images/classAjouterMembres.jpg
    :width: 60%
    :align: center
    
    Ce à quoi ressemble la page une fois que des membres ont été rajoutés
    
Au contraire, si aucun utilisateur n'a été trouvé ou si l'utilisateur ne
correspond pas au rôle qu'il lui est donné (par exemple si c'est un
professeur et qu'il a été ajouté aux étudiants), le site renvoiera un message
d'erreur.

..  figure:: images/classAjouterMembresEchec.jpg
    :width: 60%
    :align: center
    
    Message d'erreur retourné si l'utilisateur n'est pas valable
    
Une fois ajouté, un membre peut facilement être retiré du groupe grâce au bouton
Retirer qui se trouve à côté de son nom.

Gérer un devoir
*****************

Un professeur peut bien évidemment donner des devoirs à son groupe.

Un devoir peut-être un exercice, un quiz ou un cours, tous les trois
pouvant avoir été créé par un autre utilisateur.

Pour assigner un devoir, il suffit de savoir l'id de l'exercice, quiz ou cours,
et de préciser grâce au menu à choix de quel type de devoir il s'agit.

..  figure:: images/classDevoir.jpg
    :width: 60%
    :align: center
    
    Différents champs à compléter pour assigner un devoir
    
Comme pour les fonctionnalités précédentes, si aucun exercice, quiz ou cours
n'a pu être associé à l'id entrée, un message d'erreur sera renvoyé.

Un devoir peut être à tout moment retiré grâce au bouton Retirer à sa droite.

Voir ses exercices
===================

Dans le menu de gauche, il y a un bouton nommé Exercices. C'est depuis cette
page que le professeur pourra voir ses exercices, ses quiz et ses cours.

..  figure:: images/exercices.jpg
    :width: 60%
    :align: center
    
    Ce à quoi ressemble la page Exercices
    
Pour chaque activité que le professeur aura créé, il pourra voir le titre qu'il
lui a donné, la date à laquelle il l'a créé et l'id qui lui sera utile s'il veut
l'assigner en tant que devoir à un de ses groupes.

Il peut bien évidemment supprimer une activité en utilisant le bouton Supprimer
se trouvant dans la dernière colonne du tableau.

Si le professeur souhaite créer une nouvelle activité, il n'a qu'à utiliser le
bouton Créer en haut du tableau qui le redirigera directement au formulaire de
création.

Changer de mot de passe
=========================

Peu importe sur quelle page il se trouve, le professeur peut accéder à un menu
déroulant en haut à droite de cette page.

..  figure:: images/menuDeroulant.jpg
    :width: 60%
    :align: center
    
    Apparence du menu déroulant
    
Dashboard amène le professeur sur l'accueil de son dashboard, Déconnexion le
déconnecte et Profil l'amène sur un formulaire de changement de mot de passe.

Pour le modifier, le professeur n'a qu'à remplir les deux champs et à valider.
Si tout a été rentré correctement, le mot de passe sera correctement modifié.

..  figure:: images/passwordSuccess.jpg
    :width: 60%
    :align: center
    
    Message pour confirmer que le changement de mot de passe a correctement eu
    lieu
    
Au contraire, s'il y a une erreur, un message d'erreur sera retourné.

..  figure:: images/passwordFail.jpg
    :width: 60%
    :align: center
    
    Message d'erreur retourné si les champs n'ont pas correctement été remplis
