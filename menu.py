import pygame, time, os #importer toute la lib de pygame et time
from pygame.locals import * #importer les classes pygame
pygame.init() #initialisation de la fenetre

def jouer():
	exec(open("./main.py").read())

largeur_fenetre = 640
hauteur_fenetre = 480

fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre), RESIZABLE) #la variable fenetre prend la fonction fenetre avec succession d'images supperposables
fond = pygame.image.load("data/menu/background640x480.jpg").convert() #fond prend la fonction image pygame importer

#chargement et collage des boutons
#l signifie que c'est le bouton effet levé
#e signifie que c'est le bouton effet enfoncé

#jouer
jouerl = pygame.image.load("data/menu/jouer levé.png").convert()
jouere = pygame.image.load("data/menu/jouer enfoncé.png").convert()

#personnages
personnagesl = pygame.image.load("data/menu/personnages levé.png").convert()
personnagese = pygame.image.load("data/menu/personnages enfoncé.png").convert()

#niveaux
niveauxl = pygame.image.load("data/menu/niveaux levé.png").convert()
niveauxe = pygame.image.load("data/menu/niveaux enfoncé.png").convert()

#démo
demol = pygame.image.load("data/menu/démo levé.png").convert()
demoe = pygame.image.load("data/menu/démo enfoncé.png").convert()

#paramètres
parametresl = pygame.image.load("data/menu/paramètres levé.png").convert()
parametrese = pygame.image.load("data/menu/paramètres enfoncé.png").convert()


#Variables stockant l'etat des boutons
buttonj = 0
buttonpa = 0
buttonpe = 0
buttond = 0
buttonn = 0

lancer_le_jeu = False

continuer = 1

while continuer : #tant que continuer vaut 1
	for event in pygame.event.get() : #pour les evenements pygames
		if event.type == QUIT : #s'il y a une action quitter continuer vaut 0 fin de boucle
			continuer = 0
		if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] > 100 and event.pos[1] < hauteur_fenetre-315 and event.pos[0] > 220 and event.pos[0] < largeur_fenetre-220 :
			print("Jouer")
			lancer_le_jeu = True
			continuer = 0
			buttonj = 0
		if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] > 175 and event.pos[1] < hauteur_fenetre-280 and event.pos[0] > 100 and event.pos[0] < largeur_fenetre-390 :
			print("Personnages")
			buttonpe = 0
		if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] > 250 and event.pos[1] < hauteur_fenetre-200 and event.pos[0] > 100 and event.pos[0] < largeur_fenetre-390 :
			print("Niveaux")
			buttonn = 0
		if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] > 325 and event.pos[1] < hauteur_fenetre-125 and event.pos[0] > 100 and event.pos[0] < largeur_fenetre-390 :
			print("Démo")
			buttond = 0
		if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] > 265 and event.pos[1] < hauteur_fenetre-185 and event.pos[0] > 450 and event.pos[0] < largeur_fenetre-40 :
			print("Paramètres")
			buttonpa = 0


		if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] > 100 and event.pos[1] < hauteur_fenetre-315 and event.pos[0] > 220 and event.pos[0] < largeur_fenetre-220 :
			print("Jouer")
			buttonj = 1
		if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] > 175 and event.pos[1] < hauteur_fenetre-280 and event.pos[0] > 100 and event.pos[0] < largeur_fenetre-390 :
			print("Personnages")
			buttonpe = 1
		if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] > 250 and event.pos[1] < hauteur_fenetre-200 and event.pos[0] > 100 and event.pos[0] < largeur_fenetre-390 :
			print("Niveaux")
			buttonn = 1
		if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] > 325 and event.pos[1] < hauteur_fenetre-125 and event.pos[0] > 100 and event.pos[0] < largeur_fenetre-390 :
			print("Démo")
			buttond = 1
		if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] > 265 and event.pos[1] < hauteur_fenetre-185 and event.pos[0] > 450 and event.pos[0] < largeur_fenetre-40 :
			print("Paramètres")
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


	pygame.display.flip() #la fenetre s'actualise

	if lancer_le_jeu == True:
		jouer()
