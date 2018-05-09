#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, time, os #importer toute la lib de pygame et time
import webbrowser
from pygame.locals import * #importer les classes pygame
pygame.init() #initialisation de la fenetre

def jouer():
	# Ecriture du fichier d'interface
#		interf.write(interface['niveau'] + '\n')
#		interf.write(interface['dernier_niveau'] + '\n')
#		interf.write(interface['dernier_score'] + '\n')
#		interf.write(interface['meilleur_score'] + '\n')
#		interf.write(interface['musique'] + '\n')
#		interf.write(interface['son'])
	interf = open("interface.txt", 'w')
	interf.write(interface['niveau'] + '\n')
	interf.write(interface['dernier_niveau'] + '\n')
	interf.write(interface['dernier_score'] + '\n')
	interf.write(interface['meilleur_score'] + '\n')
	interf.write(interface['musique'] + '\n')
	interf.write(interface['son'])
	interf.close()
	del interf

	# Lancement du jeu
	exec(open("main.py").read())



# Lecture du fichier interface
#with open("interface.txt") as f:
#    content = f.readlines()

f = open("interface.txt", 'r')
content = f.readlines()
f.close()
del f
# Supression des '\n' a la fin des lignes
# for x in content parcours content. La boucle dans les crochets rends le code plus compact.
# x.strip() retourne une copie de x sans les espaces ou les retours a la ligne
content = [x.strip() for x in content]
interface = {'niveau':content[0], 'dernier_niveau':content[1], 'dernier_score':content[2], 'meilleur_score':content[3], 'musique':content[4], 'son':content[5]}


# musique et effets sonores
musicmenu = "data/sounds/MainMusicAcc.wav"
Stouchedown = "data/sounds/touchedown.wav"
Stoucheup = "data/sounds/toucheup.wav"
pygame.mixer.music.load(musicmenu)
if interface['musique'] == 'OFF':
	pygame.mixer.music.set_volume(0)
elif interface['musique'] == 'ON':
	pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)
touchesounddown = pygame.mixer.Sound(Stouchedown)
touchesoundup = pygame.mixer.Sound(Stoucheup)

# Dimentions fenetre
largeur_fenetre = 640
hauteur_fenetre = 480

fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre), RESIZABLE) #la variable fenetre prend la fonction fenetre avec succession d'images supperposables
fond = pygame.image.load("data/menu/background640x480.jpg").convert() #fond prend la fonction image pygame importer

#chargement des images des boutons


# numero
un = pygame.image.load("data/menu/1.png").convert()
deux = pygame.image.load("data/menu/2.png").convert()
trois = pygame.image.load("data/menu/3.png").convert()
quatre = pygame.image.load("data/menu/4.png").convert()

# cadenas
cadenasl = pygame.image.load("data/menu/cadenas leve.png").convert()
cadenase = pygame.image.load("data/menu/cadenas enfonce.png").convert() # Inutile

# jouer1
jouer1l = pygame.image.load("data/menu/play leve.png").convert()
jouer1e = pygame.image.load("data/menu/play enfonce.png").convert()
xbuttonj1 = 130
ybuttonj1 = 160
Lbuttonj1 = 150 #longueur
lbuttonj1 = 30 #largeur

#jouer2
jouer2l = pygame.image.load("data/menu/play leve.png").convert()
jouer2e = pygame.image.load("data/menu/play enfonce.png").convert()
xbuttonj2 = 130
ybuttonj2 = 220
Lbuttonj2 = 150
lbuttonj2 = 30

#jouer3
jouer3l = pygame.image.load("data/menu/play leve.png").convert()
jouer3e = pygame.image.load("data/menu/play enfonce.png").convert()
xbuttonj3 = 130
ybuttonj3 = 280
Lbuttonj3 = 150
lbuttonj3 = 30

#jouer4
jouer4l = pygame.image.load("data/menu/play leve.png").convert()
jouer4e = pygame.image.load("data/menu/play enfonce.png").convert()
xbuttonj4 = 130
ybuttonj4 = 340
Lbuttonj4 = 150
lbuttonj4 = 30

#volume
volumeon = pygame.image.load("data/menu/volume on.png").convert()
volumeoff = pygame.image.load("data/menu/volume off.png").convert()
xbuttonv = 370
ybuttonv = 400
Lbuttonv = 30
lbuttonv = 30

#musique
musiqueon = pygame.image.load("data/menu/musique on.png").convert()
musiqueoff = pygame.image.load("data/menu/musique off.png").convert()
xbuttonm = 430
ybuttonm = 400
Lbuttonm = 30
lbuttonm = 30

#info
infol = pygame.image.load("data/menu/pi leve.png").convert()
infoe = pygame.image.load("data/menu/pi enfonce.png").convert()
xbuttoninfo = 490
ybuttoninfo = 400
Lbuttoninfo = 30
lbuttoninfo = 30

#cup
cupl = pygame.image.load("data/menu/coupe levee.png").convert()
cupe = pygame.image.load("data/menu/coupe enfoncee.png").convert()
xbuttoncup = 550
ybuttoncup = 400
Lbuttoncup = 30
lbuttoncup = 30


#jamesadventure
jamesadventure = pygame.image.load("data/menu/jamesadventure.png").convert()
xbuttonja = 170
ybuttonja = 30
Lbuttonja = 300
lbuttonja = 50

# Affichage des scores
basicfont = pygame.font.SysFont(None, 36)
score = basicfont.render('Score : ' + interface['dernier_score'], True, (255, 255, 255))
scorerect = score.get_rect()
scorerect.centerx = 450
scorerect.centery = 220
highscore = basicfont.render('Meilleur Score : ' + interface['meilleur_score'], True, (255, 255, 255))
highscorerect = score.get_rect()
highscorerect.centerx = 410
highscorerect.centery = 280

#Variables stockant l'etat des boutons
buttonj1 = 0
buttonv = 0
buttonm = 0
buttonj2 = 0
buttonja = 0
buttonj3 = 0
buttonj4 = 0
buttoninfo = 0
buttoncup = 0

lancer_le_jeu = False

continuer = 1

while continuer : #tant que continuer vaut 1
	for event in pygame.event.get() : #pour les  evenements pygames
		if event.type == QUIT : #s'il y a une action quitter continuer vaut 0 fin de boucle
			continuer = 0
		if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] > ybuttonj1 and event.pos[1] < ybuttonj1+lbuttonj1 and event.pos[0] > xbuttonj1 and event.pos[0] < xbuttonj1+Lbuttonj1 :
			if interface['son'] == 'ON':
				touchesoundup.play()
			if int(interface['dernier_niveau']) >= 0: # On verifie que le niveau n'est pas verouille
				print("Niveau 1")
				interface['niveau'] = '1' # Si oui on modifie le numero du niveau a lancer
				lancer_le_jeu = True # Et on lance le prossesus pour lancer le jeu
				continuer = 0 # On ne continue pas la boucle
			buttonj1 = 0
		if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] > ybuttonj2 and event.pos[1] < ybuttonj2+lbuttonj2 and event.pos[0] > xbuttonj2 and event.pos[0] < xbuttonj2+Lbuttonj2 :
			if int(interface['dernier_niveau']) >= 1:
				print("Niveau 2")
				interface['niveau'] = '2'
				lancer_le_jeu = True
				continuer = 0
			if interface['son'] == 'ON':
				touchesoundup.play()
			buttonj2 = 0
		if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] > ybuttonj3 and event.pos[1] < ybuttonj3+lbuttonj3 and event.pos[0] > xbuttonj3 and event.pos[0] < xbuttonj3+Lbuttonj3 :
			if int(interface['dernier_niveau']) >= 2:
				print("Niveau 3")
				interface['niveau'] = '3'
				lancer_le_jeu = True
				continuer = 0
			if interface['son'] == 'ON':
				touchesoundup.play()
			buttonj3 = 0
		if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] > ybuttonj4 and event.pos[1] < ybuttonj4+lbuttonj4 and event.pos[0] > xbuttonj4 and event.pos[0] < xbuttonj4+Lbuttonj4 :
			if int(interface['dernier_niveau']) >= 3:
				print("Niveau 4")
				interface['niveau'] = '4'
				lancer_le_jeu = True
				continuer = 0
			if interface['son'] == 'ON':
				touchesoundup.play()
			buttonj4 = 0
		if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] > ybuttonv and event.pos[1] < ybuttonv+lbuttonv and event.pos[0] > xbuttonv and event.pos[0] < xbuttonv+Lbuttonv :
			print("Volume")
			if interface['son'] == 'OFF':
				interface['son'] = 'ON'
			elif interface['son'] == 'ON':
				interface['son'] = 'OFF'
			if interface['son'] == 'ON':
				touchesoundup.play()
			buttonv = 0
		if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] > ybuttonm and event.pos[1] < ybuttonm+lbuttonm and event.pos[0] > xbuttonm and event.pos[0] < xbuttonm+Lbuttonm :
			print("Musique")
			if interface['musique'] == 'OFF':
				interface['musique'] = 'ON'
				pygame.mixer.music.set_volume(0.25)
			elif interface['musique'] == 'ON':
				interface['musique'] = 'OFF'
				pygame.mixer.music.set_volume(0)
			if interface['son'] == 'ON':
				touchesoundup.play()
			buttonm = 0
		if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] > ybuttoninfo and event.pos[1] < ybuttoninfo+lbuttoninfo and event.pos[0] > xbuttoninfo and event.pos[0] < xbuttoninfo+Lbuttoninfo :
			print("Info")
			if interface['son'] == 'ON':
				touchesoundup.play()
			webbrowser.open('https://github.com/timwinner/jamesadventure')
			buttoninfo = 0
		if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] > ybuttoncup and event.pos[1] < ybuttoncup+lbuttoncup and event.pos[0] > xbuttoncup and event.pos[0] < xbuttoncup+Lbuttoncup :
			print("Coupe")
			if interface['son'] == 'ON':
				touchesoundup.play()
			buttoncup = 0


		if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] > ybuttonj1 and event.pos[1] < ybuttonj1+lbuttonj1 and event.pos[0] > xbuttonj1 and event.pos[0] < xbuttonj1+Lbuttonj1 :
			if interface['son'] == 'ON':
				touchesounddown.play()
			buttonj1 = 1

		if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] >ybuttonj2 and event.pos[1] < ybuttonj2+lbuttonj2 and event.pos[0] > xbuttonj2 and event.pos[0] < xbuttonj2+Lbuttonj2 :
			if interface['son'] == 'ON':
				touchesounddown.play()
			buttonj2 = 1

		if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] > ybuttonj3 and event.pos[1] < ybuttonj3+lbuttonj3 and event.pos[0] > xbuttonj3 and event.pos[0] < xbuttonj3+Lbuttonj3 :
			if interface['son'] == 'ON':
				touchesounddown.play()
			buttonj3 = 1

		if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] > ybuttonj4 and event.pos[1] <ybuttonj4+lbuttonj4 and event.pos[0] > xbuttonj4 and event.pos[0] < xbuttonj4+Lbuttonj4 :
			if interface['son'] == 'ON':
				touchesounddown.play()
			buttonj4 = 1

		if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] > ybuttonv and event.pos[1] < ybuttonv+lbuttonv and event.pos[0] > xbuttonv and event.pos[0] < xbuttonv+Lbuttonv :
			if interface['son'] == 'ON':
				touchesounddown.play()
			buttonv = 1

		if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] > ybuttonm and event.pos[1] < ybuttonm+lbuttonm and event.pos[0] > xbuttonm and event.pos[0] < xbuttonm+Lbuttonm :
			if interface['son'] == 'ON':
				touchesounddown.play()
			buttonm = 1

		if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] > ybuttoninfo and event.pos[1] < ybuttoninfo+lbuttoninfo and event.pos[0] > xbuttoninfo and event.pos[0] < xbuttoninfo+Lbuttoninfo :
			if interface['son'] == 'ON':
				touchesounddown.play()
			buttoninfo = 1

		if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] > ybuttoncup and event.pos[1] < ybuttoncup+lbuttoncup and event.pos[0] > xbuttoncup and event.pos[0] < xbuttoncup+Lbuttoncup :
			if interface['son'] == 'ON':
				touchesounddown.play()
			buttoncup = 1

	# Affichage des images statiques
	fenetre.blit(fond, (0,0))
	fenetre.blit(jamesadventure, (170,30))
	fenetre.blit(un, (xbuttonj1-60, ybuttonj1))
	fenetre.blit(deux, (xbuttonj2-60, ybuttonj2))
	fenetre.blit(trois, (xbuttonj3-60, ybuttonj3))
	fenetre.blit (quatre, (xbuttonj4-60, ybuttonj4))
	fenetre.blit(score, scorerect)
	fenetre.blit(highscore, highscorerect)


	if int(interface['dernier_niveau']) >= 0:
		if buttonj1 == 1:
			fenetre.blit(jouer1e, (xbuttonj1,ybuttonj1))
		else:
			fenetre.blit(jouer1l, (xbuttonj1,ybuttonj1))
	else:
		fenetre.blit(cadenasl, (xbuttonj1,ybuttonj1))

	if int(interface['dernier_niveau']) >= 1:
		if buttonj2 == 1:
			fenetre.blit(jouer2e, (xbuttonj2,ybuttonj2))
		else:
			fenetre.blit(jouer2l, (xbuttonj2,ybuttonj2))
	else:
		fenetre.blit(cadenasl, (xbuttonj2,ybuttonj2))

	if int(interface['dernier_niveau']) >= 2:
		if buttonj3 == 1:
			fenetre.blit(jouer3e, (xbuttonj3, ybuttonj3))
		else:
			fenetre.blit(jouer3l, (xbuttonj3, ybuttonj3))
	else:
		fenetre.blit(cadenasl, (xbuttonj3, ybuttonj3))

	if int(interface['dernier_niveau']) >= 3:
		if buttonj4 == 1:
			fenetre.blit(jouer4e, (xbuttonj4, ybuttonj4))
		else:
			fenetre.blit(jouer4l, (xbuttonj4, ybuttonj4))
	else:
		fenetre.blit(cadenasl, (xbuttonj4, ybuttonj4))

	if interface['son'] == 'OFF':
		fenetre.blit(volumeoff, (xbuttonv, ybuttonv))
	else:
		fenetre.blit(volumeon, (xbuttonv, ybuttonv))

	if interface['musique'] == 'OFF':
		fenetre.blit(musiqueoff, (xbuttonm, ybuttonm))
	else:
		fenetre.blit(musiqueon, (xbuttonm, ybuttonm))

	if buttoninfo == 1:
		fenetre.blit(infoe, (xbuttoninfo, ybuttoninfo))
	else:
		fenetre.blit(infol, (xbuttoninfo, ybuttoninfo))

	if buttoncup == 1:
		fenetre.blit(cupe, (xbuttoncup, ybuttoncup))
	else:
		fenetre.blit(cupl, (xbuttoncup, ybuttoncup))





	pygame.display.flip() #la fenetre s'actualise

	if lancer_le_jeu == True:
		jouer()

	time.sleep(0.03) # On laisse le temps au prosesseur de faire d'autres choses
