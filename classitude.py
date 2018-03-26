import pygame
import time
from pygame.locals import * 
from constantes import *
 
class Perso:
	def __init__(self, droites, gauches, droite1, droite2, gauche1, gauche2):
		self.droites = pygame.image.load(droites).convert_alpha()
		self.gauches = pygame.image.load(gauches).convert_alpha()
		self.hautd = pygame.image.load(droite2).convert_alpha()
		self.hautg = pygame.image.load(gauche2).convert_alpha()
		self.droite1 = pygame.image.load(droite1).convert_alpha()
		self.droite2 = pygame.image.load(droite2).convert_alpha()
		self.gauche1 = pygame.image.load(gauche1).convert_alpha()
		self.gauche2 = pygame.image.load(gauche2).convert_alpha()
		
		self.x = 0
		self.y = 0
		self.vitesse_x = 0
		self.vitesse_y = 0

		self.dplc = 0
		self.direction = self.droites
#		'''self.niveau = niveau'''
	
	
	def deplacer(self, direction, plateforme):		
		#droite
		if direction[0] == 1:
			if plateforme.onPlateforme(self.x + largeur_hero + v_dplc, self.y) == False and plateforme.onPlateforme(self.x + largeur_hero + v_dplc, self.y + taille_hero) == False:
				self.x += v_dplc
			if self.dplc % v_dplc == 0 :
				self.direction = self.droites
			elif self.dplc % v_dplc == 2 :
				self.direction = self.droite1
			elif self.dplc % v_dplc == 4 :
				self.direction = self.droite2

		#gauche
		if direction[1] == 1:
			if self.x > 0 and plateforme.onPlateforme(self.x + v_dplc, self.y) == False and plateforme.onPlateforme(self.x + v_dplc, self.y + taille_hero) == False:
				self.x -= v_dplc
			if self.dplc % v_dplc == 0 :
				self.direction = self.gauches
			elif self.dplc % v_dplc == 2 :
				self.direction = self.gauche1
			elif self.dplc % v_dplc == 4 :
				self.direction = self.gauche2

		#haut
		if direction[2] == 1:
			if self.y == hauteur_fenetre - taille_hero or self.vitesse_y == 0:
				self.vitesse_y -= gravity
			if self.direction == self.droites or self.direction == self.droite1 or self.direction == self.droite2 :
				self.direction = self.hautd
			elif self.direction == self.gauches or self.direction == self.gauche1 or self.direction == self.gauche2 : 
				self.direction = self.hautg
		#bas
		if direction[3] == 1:
			self.vitesse_y += 5
		
		self.dplc += 1
		if (direction[0] == 0 and direction[1] == 0) or (direction[1] == 1 and direction[0]== 1) :
			self.dplc = 0
	
		self.vitesse_y += 1
		
		if  self.y + self.vitesse_y < hauteur_fenetre - taille_hero and plateforme.onPlateforme(self.x, self.y + self.vitesse_y + taille_hero) == False and plateforme.onPlateforme(self.x + largeur_hero, self.y + self.vitesse_y + taille_hero) == False:
			if plateforme.onPlateforme(self.x, self.y + self.vitesse_y) == False and plateforme.onPlateforme(self.x + largeur_hero, self.y + self.vitesse_y) == False :
				self.y = self.y + self.vitesse_y
		else:
#			self.y = hauteur_fenetre - taille_hero
			self.vitesse_y = 0



class Projectile:
	def __init__(self, x, y , haut, droite, gauche, direct):
		self.haut = pygame.image.load(haut).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.droite = pygame.image.load(droite).convert_alpha()
		self.shoot = True
		if direct[0] == 1:
			self.x = x + largeur_hero
			self.y = y + 5
			self.direction = self.droite
		if direct[1] == 1:
			self.x = x
			self.y = y + 5
			self.direction = self.gauche
		if direct[2] == 1:
			self.x = x + largeur_hero
			self.y = y -10
			self.direction = self.haut


	def tir(self, tir):
		self.shoot = tir
		#droite
		if self.direction == self.droite:
			if self.x < largeur_fenetre :
				self.x += 20
			else :
				self.shoot = False
		#gauche
		if self.direction == self.gauche:
			if self.x > 0:
				self.x -= 20
			else :
				self.shoot = False
		#haut
		if self.direction == self.haut:
			if self.y > 0:
				self.y -= 20
			else :
				self.shoot = False



# Classe gerant l'affichage des plateformes			
class Plateformes:
	#
	def __init__(self,fenetre, level):
		self.fichier = level
		#On ouvre le fichier
		with open(self.fichier, "r") as fichier: # on ouvre le fichier de niveau
			structure_niveau = []
			#On parcourt les lignes du fichier
			for ligne in fichier:
				ligne_niveau = []
				#On parcourt les blocs (lettres) contenus dans le fichier
				for block in ligne:
					#On ignore les "\n" de fin de ligne
					if block != '\n':
						#On ajoute le bloc à la liste de la ligne
						ligne_niveau.append(block)
				#On ajoute la ligne à la liste du niveau
				structure_niveau.append(ligne_niveau)
			#On sauvegarde cette structure
			self.structure = structure_niveau
			
			
	def afficher(self, fenetre):
		#Chargement des images 
		plateforme = pygame.image.load(image_plateforme).convert()
		
		#On parcourt la liste du niveau
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				#On calcule la position réelle en pixels
				x = num_case * taille_plateforme
				y = num_ligne * taille_plateforme
				if sprite == 'm':		   #m = Mur
					fenetre.blit(plateforme, (x,y)) # On affiche la plateforme sur la fenetre
				num_case += 1
			num_ligne += 1
	
	def onPlateforme(self, x, y):
		onPlateforme = False
		
		# division entière pour trouver le bloc dans leauel se trouve le point (x; y)
		blocx = x // taille_plateforme # division entière pour trouver le bloc dans leauel se trouve le point (x; y)
		blocy = y // taille_plateforme
		
		# On regarde si un bloc 'm' de trouve à l'emplacement du bloc qui contient (x; y)
		if blocx < len(self.structure[1]) and blocy < len(self.structure) : # On évite l'erreur out of range
			if self.structure[blocy][blocx] == 'm':
				onPlateforme = True
			
		if blocx >= len(self.structure[1]) and blocy >= len(self.structure) : # On considère la sortie de la fenêtre comme un bloc
			onPlateforme = True
			
		return onPlateforme
			
