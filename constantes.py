#!/usr/bin/env python
# -*- coding: utf-8 -*-

			#les differentes constantes utilisees

#  Variables depreciees
largeur_fenetre = 1080
hauteur_fenetre = 600
#1920x1080 lycee, 1366x758 maison, 640x480 pour plateformes

# Constantes de jeu
taille_hero = 31
largeur_hero = 25
v_dplc = 6 # vitesse de deplacement du personnage
gravity = 15
taille_plateforme = 40
vitesse_projectile = 19

			#les differentes images utilisees
# Images james
pgauches = "data/images/jamesstatiquegauche.png" # Static
pgauched1 = "data/images/jamesdeplacementgauche1.png" # Mouvement
pgauched2 = "data/images/jamesdeplacementgauche2.png" # Mouvement
pdroited1 = "data/images/jamesdeplacementdroite1.png" # Mouvement
pdroited2 = "data/images/jamesdeplacementdroite2.png" # Mouvement
pdroites = "data/images/jamesstatiquedroite.png" # Static
phaut = "data/images/jamesstatiquedroite.png" # Saut

# Images boule de feu
bgauche = "data/images/tirgauche.png"
bdroite = "data/images/tirdroite.png"
bhaut = "data/images/tirhaut.png"

background = "data/images/background_futur.jpg" # Image de fond
image_plateforme = "data/images/plateforme2.png" # Images d'une plateforme
image_portal = "data/images/portal1.png"


# Dictionnaires stockant toutes les information des niveaux
l1 = {'file':'data/levels/l1.txt', 'background':'data/images/background640x480.jpg', 'width':640, 'height':480, 'platform':'data/images/plateforme2.png'}
l2 = {'file':'data/levels/l2.txt', 'background':'data/images/background_futur.jpg', 'width':1080, 'height':600, 'platform':'data/images/plateforme2.png'}
l3 = {'file':'data/levels/l3.txt', 'background':'data/images/background640x480.jpg', 'width':640, 'height':480, 'platform':'data/images/plateforme2.png'}


#Musiques et sons
musicprinc = "data/sounds/MainMusicAll.wav"
musicmenu = "data/sounds/MainMusicAcc.wav"
