{"filter":false,"title":"urls.py","tooltip":"/source/code/urls.py","undoManager":{"mark":10,"position":10,"stack":[[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":15,"column":1},"action":"insert","lines":["from django.conf.urls import patterns, include, url","from django.contrib import admin","from dashboard.views import *","","","urlpatterns = patterns('teachers.views',","    url(r'^home/$', home, name='home'),","    url(r'^classe/(?P<group_id>\\d+)/$', group, name='group_view'),","    url(r'^login/$', login, name='login'),","    url(r'^exercices/$', exercises, name='exercises'),","    url(r'^nouveau_groupe/$', newgroup, name='newgroup'),","    url(r'^profil/$', profil, name = 'profil'),","    url(r'^enlever_groupe/(?P<group_id>\\d+)/(?P<member_id>\\d+)/$', deleteFromGroup, name = \"deleteFromGroup\"),","    url(r'^enlever_activité/(?P<activity_id>\\d+)/$', deleteActivity, name = \"deleteActivity\"),","    url(r'^enlever_devoir/(?P<group_id>\\d+)/(?P<homework_id>\\d+)/$', deleteHomework, name = \"deleteHomework\"),",")"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"remove","lines":["    url(r'^login/$', login, name='login'),",""]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":14,"column":1},"action":"remove","lines":["from django.conf.urls import patterns, include, url","from django.contrib import admin","from dashboard.views import *","","","urlpatterns = patterns('teachers.views',","    url(r'^home/$', home, name='home'),","    url(r'^classe/(?P<group_id>\\d+)/$', group, name='group_view'),","    url(r'^exercices/$', exercises, name='exercises'),","    url(r'^nouveau_groupe/$', newgroup, name='newgroup'),","    url(r'^profil/$', profil, name = 'profil'),","    url(r'^enlever_groupe/(?P<group_id>\\d+)/(?P<member_id>\\d+)/$', deleteFromGroup, name = \"deleteFromGroup\"),","    url(r'^enlever_activité/(?P<activity_id>\\d+)/$', deleteActivity, name = \"deleteActivity\"),","    url(r'^enlever_devoir/(?P<group_id>\\d+)/(?P<homework_id>\\d+)/$', deleteHomework, name = \"deleteHomework\"),",")"]},{"start":{"row":0,"column":0},"end":{"row":17,"column":1},"action":"insert","lines":["from django.conf.urls import patterns, include, url","from django.contrib import admin","from dashboard.views import *","","","urlpatterns = patterns('teachers.views',","    url(r'^home/$', home, name='home'),","    url(r'^classe/(?P<group_id>\\d+)/$', group, name='group_view'),","    url(r'^exercices/$', exercises, name='exercises'),","    url(r'^nouveau_groupe/$', newgroup, name='newgroup'),","    url(r'^profil/$', profil, name = 'profil'),","    #Pour retirer d'un groupe","    url(r'^enlever_groupe/(?P<group_id>\\d+)/(?P<member_id>\\d+)/$', deleteFromGroup, name = \"deleteFromGroup\"),","    #Pour supprimer une activité","    url(r'^enlever_activité/(?P<activity_id>\\d+)/$', deleteActivity, name = \"deleteActivity\"),","    #Pour retirer un devoir","    url(r'^enlever_devoir/(?P<group_id>\\d+)/(?P<homework_id>\\d+)/$', deleteHomework, name = \"deleteHomework\"),",")"]}]}],[{"group":"doc","deltas":[{"start":{"row":14,"column":53},"end":{"row":15,"column":0},"action":"insert","lines":["",""]},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":15,"column":4},"end":{"row":15,"column":8},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":66},"end":{"row":12,"column":67},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":66},"end":{"row":13,"column":0},"action":"insert","lines":["",""]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":4},"end":{"row":13,"column":8},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":68},"end":{"row":18,"column":69},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":68},"end":{"row":19,"column":0},"action":"insert","lines":["",""]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":19,"column":4},"end":{"row":19,"column":8},"action":"insert","lines":["    "]}]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":30.39125,"selection":{"start":{"row":19,"column":8},"end":{"row":19,"column":8},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1427355569124,"hash":"a11ab4ecd227bc5d4c89eff92c3e0d5ea2f4b81a"}