Baudin Stanislas 195344 -
Irankunda Régis 195311



Dans le cadre du cours B2160-Projet informatique, nous avons du créer une intelligence artificielle opérant sur le jeu AVALAM.


Dans ce dossier, vous pouvez trouvez:
	
  inscription.py: fonction qui va permettre de se connecteur au serveur 
	
  avalamV1.py: fonction qui contient notre IA


Pour lancer notre IA sur le server (https://github.com/Seb1903/AvalamAI/tree/master/AIGameRunner-master), vous devez:

lancer inscription.py dans l'invité de commande("python inscription.py") en vous assurant que le port 8082 est 
libre. 

Une fois l'inscription faite, c'est au tour d'avalamV1.py d'être lancé dans l'invité de commande("python avalamV1.py")


La stratégie de notre IA est simple, elle ne joue pas en envisageant les coups à l'avance. Dès qu'elle a l'occasion de faire une tour de 5 avec les pions de l'adversaire, elle le fait sinon elle fait une simple tour.
Son but ne va pas être de faire le plus de tour de 5 mais le plus de tours tout court au détriment de son adversaire.


Enjoy!
