#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, time, os #importer toute la lib de pygame et time
from pygame.locals import * #importer les classes pygame
from constantes import * #importer les constantes (ici pour la musique)
pygame.init() #initialisation de la fenetre


def jouer():
	exec(open("main.py").read())




# Lecture du fichier interface

with open("interface.txt") as f:
    content = f.readlines()
# Supression des '\n' a la fin des lignes
# for x in content parcours content. La boucle dans les crochets rends le code plus compact.
# x.strip() retourne une copie de x sans les espaces ou les retours a la ligne
content = [x.strip() for x in content]
interface = {'niveau':content[0], 'dernier_niveau':content[1], 'dernier_score':content[2], 'meilleur_score':content[3], 'musique':content[4], 'son':content[5]}

print(str(interface))

# Dimessions de la fenetre du menu
largeur_fenetre = 640
hauteur_fenetre = 480

# la variable fenetre prend la fonction fenetre avec succession d'images supperposables
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
# fond prend la fonction image pygame importer
fond = pygame.image.load("data/menu/background640x480.jpg").convert()

# chargement et collage des boutons
# l signifie que c'est le bouton effet leve
# e signifie que c'est le bouton effet enfonce

# jouer
jouerl = pygame.image.load("data/menu/jouer leve.png").convert()
jouere = pygame.image.load("data/menu/jouer enfonce.png").convert()

# personnages
personnagesl = pygame.image.load("data/menu/personnages leve.png").convert()
personnagese = pygame.image.load("data/menu/personnages enfonce.png").convert()

# niveaux
niveauxl = pygame.image.load("data/menu/niveaux leve.png").convert()
niveauxe = pygame.image.load("data/menu/niveaux enfonce.png").convert()

# demo
demol = pygame.image.load("data/menu/demo leve.png").convert()
demoe = pygame.image.load("data/menu/demo enfonce.png").convert()

# parametres
parametresl = pygame.image.load("data/menu/parametres leve.png").convert()
parametrese = pygame.image.load("data/menu/parametres enfonce.png").convert()


# Variables stockant l'etat des boutons
buttonj = 0
buttonpa = 0
buttonpe = 0
buttond = 0
buttonn = 0

lancer_le_jeu = False

continuer = 1

#musique :
pygame.mixer.music.load(musicmenu)
pygame.mixer.music.set_volume(0.075)
pygame.mixer.music.play(-1)

#son
touchesounddown = pygame.mixer.Sound(Stouchedown)
touchesoundup = pygame.mixer.Sound(Stoucheup)

while continuer : # tant que continuer vaut 1
	for event in pygame.event.get() : # pour les evenements pygames
		if event.type == QUIT : # s'il y a une action quitter continuer vaut 0 fin de boucle
			continuer = 0

			pygame.mixer.music.stop()


		if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] > 100 and event.pos[1] < hauteur_fenetre-315 and event.pos[0] > 220 and event.pos[0] < largeur_fenetre-220 :
			touchesounddown.play()
			print("Jouer")
			lancer_le_jeu = True
			continuer = 0
			buttonj = 0

		if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] > 175 and event.pos[1] < hauteur_fenetre-280 and event.pos[0] > 100 and event.pos[0] < largeur_fenetre-390 :
			touchesounddown.play()
			print("Personnages")
			buttonpe = 0
		if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] > 250 and event.pos[1] < hauteur_fenetre-200 and event.pos[0] > 100 and event.pos[0] < largeur_fenetre-390 :
			touchesounddown.play()
			print("Niveaux")
			buttonn = 0
		if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] > 325 and event.pos[1] < hauteur_fenetre-125 and event.pos[0] > 100 and event.pos[0] < largeur_fenetre-390 :
			touchesounddown.play()
			print("Demo")
			buttond = 0
			touchesounddown.play()
		if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] > 265 and event.pos[1] < hauteur_fenetre-185 and event.pos[0] > 450 and event.pos[0] < largeur_fenetre-40 :
			touchesounddown.play()
			print("Parametres")
			buttonpa = 0


		if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] > 100 and event.pos[1] < hauteur_fenetre-315 and event.pos[0] > 220 and event.pos[0] < largeur_fenetre-220 :
			touchesoundup.play()
			print("Jouer")
			buttonj = 1
		if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] > 175 and event.pos[1] < hauteur_fenetre-280 and event.pos[0] > 100 and event.pos[0] < largeur_fenetre-390 :
			touchesoundup.play()
			print("Personnages")
			buttonpe = 1
		if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] > 250 and event.pos[1] < hauteur_fenetre-200 and event.pos[0] > 100 and event.pos[0] < largeur_fenetre-390 :
			touchesoundup.play()
			print("Niveaux")
			buttonn = 1
		if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] > 325 and event.pos[1] < hauteur_fenetre-125 and event.pos[0] > 100 and event.pos[0] < largeur_fenetre-390 :
			touchesoundup.play()
			print("Démo")
			buttond = 1
		if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] > 265 and event.pos[1] < hauteur_fenetre-185 and event.pos[0] > 450 and event.pos[0] < largeur_fenetre-40 :
			touchesoundup.play()
			print("Parametres")
			buttonpa = 1


	fenetre.blit(fond, (0,0))
	if buttonj == 1:
		fenetre.blit(jouere, (220,100))
	else:
		fenetre.blit(jouerl, (220,100))

	if buttonpe == 1:
		fenetre.blit(personnagese, (100,175))
	else:
		fenetre.blit(personnagesl, (100,175))

	if buttonn == 1:
		fenetre.blit(niveauxe, (100, 250))
	else:
		fenetre.blit(niveauxl, (100, 250))

	if buttond == 1:
		fenetre.blit(demoe, (100,325))
	else:
		fenetre.blit(demol, (100,325))

	if buttonpa == 1:
		fenetre.blit(parametrese, (450, 265))
	else:
		fenetre.blit(parametresl, (450, 265))


	pygame.display.flip() # la fenetre s'actualise

	if lancer_le_jeu == True:
		jouer()

	time.sleep(0.01)
