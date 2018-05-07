#import des librairies
import pygame
import time
from pygame.locals import *
from classitude import *
from constantes import *

pygame.init() # Initialisation de pygame

# Lecture du niveau séléctionné dans interface.txt
interface = open('interface.txt', 'r')
numlvl = interface.read(1)
if numlvl == '1':
	level = l1
if numlvl == '2':
	level = l2
if numlvl == '3':
	level = l3

# création de la fenetre et du fond de la fenetre
fenetre = pygame.display.set_mode((level['width'], level['height']), RESIZABLE)
fond = pygame.image.load(level['background']).convert()
fenetre.blit(fond, (0,0)) # On place le fond sur la fenêtre

# création du personnage avec ces différentes images :
#position droite statique, de déplacement 1 et 2 et position gauche statique, de déplacement 1 et 2
james = Perso(pdroites, pgauches, pdroited1, pdroited2, pgauched1, pgauched2)

#création des plateformes
plateformes = Plateformes(fenetre, level['file'])

pygame.display.flip() # Raffraichissement de l'affichage après l'init

#initialisation des variables
continuer = 1
keyState = [0, 0, 0, 0] # état du personnage lors de l'appuie d'une touche, respectivement droite, gauche, haut et bas
dirPer = [0,0,0] # direction du personnage, pour avoir la direction de la boule : droite, gauche, haut
tir = False

#musique :
pygame.mixer.music.load(musicprinc)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.75)

#son
sonsaut = pygame.mixer.Sound(Ssaut)
sontir = pygame.mixer.Sound(Stir)

while continuer:
	pygame.time.Clock().tick(30)


	#test pygame pour...
	for event in pygame.event.get():

		# ...pour un évènement de quitte
		if event.type == QUIT:
			continuer = 0
			pygame.mixer.music.stop()

		# ...pour un évènement de touche enfoncée
		elif event.type == KEYDOWN:
			if event.key == K_RIGHT :
				keyState[0] = 1
			elif event.key == K_d :
				keyState[0] = 1
			elif event.key == K_LEFT:
				keyState[1] = 1
			elif event.key == K_a:
				keyState[1] = 1
			elif event.key == K_UP:
				sonsaut.play()
				keyState[2] = 1
			elif event.key == K_w:
				sonsaut.play()
				keyState[2] = 1
			elif event.key == K_DOWN:
				keyState[3] = 1
			elif event.key == K_s:
				keyState[3] = 1

			# ...pour un évènement sur la barre espace : tir
			elif event.key == K_SPACE :
				if tir == False :
					sontir.play()
					if james.direction == james.droites or james.direction == james.droite1 or james.direction == james.droite2 or james.direction == james.hautd:
						dirPer[0] = 1
					if james.direction == james.gauches or james.direction == james.gauche1 or james.direction == james.gauche2 or james.direction == james.hautg:
						dirPer[1] = 1
					if james.direction == james.hautd or james.direction == james.hautg :
						dirPer[2] = 1

					boule = Projectile(james.x, james.y, bhaut, bdroite, bgauche, dirPer)
					dirPer = [0,0,0]
					tir = boule.shoot

		# ...pour un évènement de touche relevé
		elif event.type == KEYUP:
			if event.key == K_RIGHT :
				keyState[0] = 0
			elif event.key == K_d :
				keyState[0] = 0
			elif event.key == K_LEFT:
				keyState[1] = 0
			elif event.key == K_a:
				keyState[1] = 0
			elif event.key == K_UP:
				keyState[2] = 0
			elif event.key == K_w:
				keyState[2] = 0
			elif event.key == K_DOWN:
				keyState[3] = 0
			elif event.key == K_s:
				keyState[3] = 0

		# ...pour un évènement avec souris : déplacement du personnage aux coordonées de la souris (si bug)
		elif event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				james.x = event.pos[0]
				james.y = event.pos[1]

	#modifications des variables pour James avec la fonction déplacer
	james.deplacer(keyState, plateformes)

	#actualisation des variables de la fenetre puis du personnage
	fenetre.blit(fond, (0,0))
	fenetre.blit(james.direction, (james.x, james.y))

	#test de tir pour la boule de feu
	if tir == True:
		boule.tir(tir, plateformes, level)
		tir = boule.shoot
		fenetre.blit(boule.direction, (boule.x, boule.y))
		#si la boule sort de l'écran, on la supprime
		if tir == False :
			del(boule)

	#affichage des plateformes
	plateformes.afficher(fenetre)

	#rafraichissement de l'application
	pygame.display.flip()

#lancement du menu du demmarage après avoir quitter le jeu
exec(open("menu.py").read())
