import pygame
import time
from pygame.locals import *
from classitude import *
from constantes import *

pygame.init()

interface = open('interface.txt', 'r')
numlvl = interface.read(1)
if numlvl == '1':
	level = l1
#	print('level is l1')
if numlvl == '2':
	level = l2
#	print('level is l2')

fenetre = pygame.display.set_mode((level['width'], level['height']), RESIZABLE)
fond = pygame.image.load(level['background']).convert()
fenetre.blit(fond, (0,0))

#création du personnage avec ces différentes images :
#position droite statique, de déplacement 1 et 2 et position gauche statique, de déplacement 1 et 2
james = Perso(pdroites, pgauches, pdroited1, pdroited2, pgauched1, pgauched2)

plateformes = Plateformes(fenetre, level['file'])

pygame.display.flip()

continuer = 1
keyState = [0, 0, 0, 0] # état du personnage lors de l'appuie d'une touche, respectivement droite, gauche, haut et bas
dirPer = [0,0,0] # direction du personnage, pour avoir la direction de la boule : droite, gauche, haut
tir = False



while continuer:
	pygame.time.Clock().tick(30)
	for event in pygame.event.get():

		# pour un évènement de quitte
		if event.type == QUIT:
			continuer = 0

		# pour un évènement de touche enfoncée
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
				keyState[2] = 1
			elif event.key == K_w:
				keyState[2] = 1
			elif event.key == K_DOWN:
				keyState[3] = 1
			elif event.key == K_s:
				keyState[3] = 1

			# pour un évènement sur la barre espace : tir
			elif event.key == K_SPACE :
				if tir == False :
					if james.direction == james.droites or james.direction == james.droite1 or james.direction == james.droite2 or james.direction == james.hautd:
						dirPer[0] = 1
					if james.direction == james.gauches or james.direction == james.gauche1 or james.direction == james.gauche2 or james.direction == james.hautg:
						dirPer[1] = 1
#					if james.direction == james.hautd or james.direction == james.hautg :
#						dirPer[2] = 1

					boule = Projectile(james.x, james.y, bhaut, bdroite, bgauche, dirPer)
					dirPer = [0,0,0]
					tir = boule.shoot

		# pour un évènement de touche relevé
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

		# pour un évènement avec souris : déplacement du personnage aux coordonées de la souris (si bug)
		elif event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				james.x = event.pos[0]
				james.y = event.pos[1]

	james.deplacer(keyState, plateformes)
	fenetre.blit(fond, (0,0))
	fenetre.blit(james.direction, (james.x, james.y))
	#test de tir pour la boule de feu
	if tir == True:
		boule.tir(tir)
		tir = boule.shoot
		fenetre.blit(boule.direction, (boule.x, boule.y))
		#si la boule sort de l'écran, on la supprime
		if tir == False :
			del(boule)

	plateformes.afficher(fenetre)

	pygame.display.flip()
