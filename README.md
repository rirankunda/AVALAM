Baudin Stanislas 195344 -
Irankunda Régis 195311



Dans le cadre du cours B2160-Projet informatique, nous avons du créer une intelligence artificielle opérant sur le jeu AVALAM.


Dans ce dossier, vous pouvez trouvez:
	
  inscription.py: fonction qui va permettre de se connecteur au serveur 
	
  avalamV1.py: fonction qui contient notre IA


Pour lancer notre IA sur le server (https://github.com/Seb1903/AvalamAI/tree/master/AIGameRunner-master), vous devez:

1) Vous assurez d'avoir cherrypy d'installé

2) lancer inscription.py dans l'invité de commande("python inscription.py [Le port ex:1234]")

3) Une fois l'inscription faite, c'est au tour d'avalam_server.py d'être lancé dans l'invité de commande("python avalam_server.py [le même port que pour inscription]")


La stratégie de notre IA est simple, elle ne joue pas en envisageant les coups à l'avance. Dès qu'elle a l'occasion de faire une tour de 5 avec les pions de l'adversaire, elle le fait sinon elle fait une simple tour.
Son but ne va pas être de faire le plus de tour de 5 mais le plus de tours tout court au détriment de son adversaire.


Enjoy!
