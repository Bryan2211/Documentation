####################
Débuter un projet
####################

Pour comprendre grâce à la pratique, nous allons au cours de ce travail établir un dashboard permettant à un
professeur de gérer des classes et des exercices sur un site d'e-learning pour les mathématiques grâce à Django, un framework fonctionnant avec Python.

Eléments requis
===============

Pour pouvoir parfaitement suivre ce guide, il nous faudra les éléments suivants afin de réaliser les tests:

*   **Django 1.7:** en effet, il va vous falloir django, car c'est le framework que l'on va utiliser. Pour le télécharger,
    il suffit de taper la commande suivante avec pip:
    ::
    
        sudo pip3 install django==1.7
        
    Si vous utilisez Windows, vous pouvez enlever *sudo*.

*   **Selenium:** Selenium est un outil permettant de gérer les navigateurs avec des commandes. Ceci nous sera utile pour les
    tests fonctionnels (ce terme sera expliqué plus tard). Encore une fois, il est possible de le télécharger grâce à pip:
    ::
    
        sudo pip3 install --upgrade selenium
        
    Encore une fois, le *sudo* n'est pas nécessaire sur Windows.
    
    Note: il est important de toujours utiliser la dernière version de Selenium. En effet, une version dépassée peut facilement se comporter de
    façon non désirée. [#f1]_
    
Une fois les éléments nécessaires installés, vous pouvez passer à la suite.

Premier test
============

Le principe de base du Test Driven Development est d'écrire un test avant même de coder ce que le test doit vérifier. Pour notre exemple,
on devrait vérifier qu'il y ait le plus basique des éléments sur notre site: Django. On va donc créer un test fonctionnel pour voir s'il y a bien
le titre de Django sur la page d'accueil. Le test fonctionnel permet de nous assurer que notre site fonctionne et possède
la fonctionnalité la plus optimale qu'il soit.

Commençons donc par écrire ce code:

..  code-block:: python
    :linenos:
    
    from selenium import webdriver
    
    browser = webdriver.Firefox()
    browser.get("http://localhost:8000")
    
    assert "Django" in browser.title
    
    browser.quit()
    
Regardons une par une les lignes qui pourrait poser des problèmes de compréhensions:

1.  Nous permet d'importer webdriver qui nous sera utile pour gérer les navigateurs web (dans ce cas, Firefox), nous permettant de les ouvrir,
    d'aller à une URL ou de les fermer.

6.  Va basiquement nous dire si la page que l'on vient de charger (http://localhost:8000) contient le mot "Django" dans le titre.

Comme on peut s'y attendre, du moins si on se rappelle du but d'un test, le test ne marchera pas. En effet, comme dit précédemment,
les tests sont faits pour évaluer quelque chose que l'on n'a pas encore fait, et pour nous aider à les faire le plus simplement possible.

**Quand on test, il ne faut pas avoir les tests qui échouent comme quelque chose de mal. Dans certains cas ( comme celui-ci),
ces tests sont attendus et recevoir un** *False* **à la fin est donc un bon signe: notre test marche!**

.. rubric:: Note de bas de page

..  [#f1] Inspiré de Test Driven Development With Python de Harry J.W. Percival