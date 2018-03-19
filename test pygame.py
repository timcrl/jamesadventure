import pygame
import time
from pygame.locals import *
from classitude import *
from constantes import *

pygame.init()

fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre), RESIZABLE) 
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))

james = Perso(pdroites, pgauches, pdroited1, pdroited2, pgauched1, pgauched2)
plateformes = Plateformes(fenetre, "l1.txt")

pygame.display.flip()

continuer = 1
keyState = [0, 0, 0, 0]
dirPer = [0,0,0]
tir = False

while continuer:
	pygame.time.Clock().tick(30)
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0

		elif event.type == KEYDOWN:
			#Touches de déplacement du perso
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
			
			elif event.key == K_SPACE : 
				if tir == False :
					if james.direction == james.droites or james.direction == james.droite1 or james.direction == james.droite2 :
						dirPer[0] = 1
					if james.direction == james.gauches or james.direction == james.gauche1 or james.direction == james.gauche2 :
						dirPer[1] = 1
					if james.direction == james.hautd or james.direction == james.hautg :
						dirPer[2] = 1

					boule = Projectile(james.x, james.y, bhaut, bdroite, bgauche, dirPer)
					dirPer = [0,0,0]
					tir = boule.shoot
		elif event.type == KEYUP:
					
		#Touches de déplacement de Donkey Kong
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

				
		elif event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				james.x = event.pos[0]
				james.y = event.pos[1]
		
	james.deplacer(keyState, plateformes)
	fenetre.blit(fond, (0,0))
	fenetre.blit(james.direction, (james.x, james.y))
	if tir == True:
		boule.tir(tir)
		tir = boule.shoot
		fenetre.blit(boule.direction, (boule.x, boule.y))
		if tir == False :	
			del(boule)
	
	plateformes.afficher(fenetre)
		
	pygame.display.flip()
