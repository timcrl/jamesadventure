# Fichier contenant les classes du jeu

# importation des librairies
import pygame
import time
from pygame.locals import *
from constantes import *

# Classe gerant le personnage principal
class Perso:
	def __init__(self, droites, gauches, droite1, droite2, gauche1, gauche2):
		#initialisation des images...
		self.droites = pygame.image.load(droites).convert_alpha()
		self.gauches = pygame.image.load(gauches).convert_alpha()
		self.hautd = pygame.image.load(droite2).convert_alpha()
		self.hautg = pygame.image.load(gauche2).convert_alpha()
		self.droite1 = pygame.image.load(droite1).convert_alpha()
		self.droite2 = pygame.image.load(droite2).convert_alpha()
		self.gauche1 = pygame.image.load(gauche1).convert_alpha()
		self.gauche2 = pygame.image.load(gauche2).convert_alpha()

		#...puis des coordonnees...
		self.x = 0
		self.y = 0
		self.vitesse_x = 0
		self.vitesse_y = 0

		#...puis des variables du personnage
		self.dplc = 0
		self.direction = self.droites



	def deplacer(self, direction, plateforme):
		#pour un deplacement a droite
		if direction[0] == 1:
			if plateforme.onPlateforme(self.x + largeur_hero + 1, self.y) == False and plateforme.onPlateforme(self.x + largeur_hero + 1, self.y + taille_hero) == False:
				self.x += v_dplc
			if self.dplc % v_dplc == 0 :
				self.direction = self.droites
			elif self.dplc % v_dplc == 2 :
				self.direction = self.droite1
			elif self.dplc % v_dplc == 4 :
				self.direction = self.droite2

		#pour un deplacement a gauche
		if direction[1] == 1:
			if self.x > 0 and plateforme.onPlateforme(self.x - 1, self.y) == False and plateforme.onPlateforme(self.x - 1, self.y + taille_hero) == False:
				self.x -= v_dplc
			if self.dplc % v_dplc == 0 :
				self.direction = self.gauches
			elif self.dplc % v_dplc == 2 :
				self.direction = self.gauche1
			elif self.dplc % v_dplc == 4 :
				self.direction = self.gauche2

		#pour un deplacement vers le haut : saut
		if direction[2] == 1:
			if self.y == hauteur_fenetre - taille_hero or self.vitesse_y == 0:
				self.vitesse_y -= gravity
			if self.direction == self.droites or self.direction == self.droite1 or self.direction == self.droite2 :
				self.direction = self.hautd
			elif self.direction == self.gauches or self.direction == self.gauche1 or self.direction == self.gauche2 :
				self.direction = self.hautg

		#pour un deplacement vers le bas
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


# Classe gerant les projectiles
class Projectile:
	def __init__(self, x, y , haut, droite, gauche, direct):
		#initialisation des images...
		self.haut = pygame.image.load(haut).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.droite = pygame.image.load(droite).convert_alpha()

		#...puis des coordonnees...
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

		#...puis des variables du projectile
		self.shoot = True

	def tir(self, tir, plateforme, level):
		self.shoot = tir

		#pour un tir a droite
		if self.direction == self.droite:
			if self.x < level['width'] and plateforme.onPlateforme(self.x + vitesse_projectile, self.y) == False:
				self.x += vitesse_projectile
			else :
				self.shoot = False

		#pour un tir a gauche
		if self.direction == self.gauche:
			if self.x > 0 and plateforme.onPlateforme(self.x - vitesse_projectile, self.y) == False:
				self.x -= vitesse_projectile
			else :
				self.shoot = False

		#pour un tir vers le haut
		if self.direction == self.haut:
			if self.y > 0 and plateforme.onPlateforme(self.x, self.y - vitesse_projectile) == False:
				self.y -= vitesse_projectile
			else :
				self.shoot = False



# Classe gerant l'affichage des plateformes
class Plateformes:
	# Initialisation
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
						#On ajoute le bloc a la liste de la ligne
						ligne_niveau.append(block)
				#On ajoute la ligne a la liste du niveau
				structure_niveau.append(ligne_niveau)
			#On sauvegarde cette structure
			self.structure = structure_niveau


	def afficher(self, fenetre):
		#Chargement de l'image de la plateforme
		plateforme = pygame.image.load(image_plateforme).convert()
		portal = pygame.image.load(image_portal).convert_alpha()

		#On parcourt la liste du niveau
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				#On calcule la position reelle en pixels
				x = num_case * taille_plateforme
				y = num_ligne * taille_plateforme
				if sprite == 'm' or sprite == 't':		   #m = Mur
					fenetre.blit(plateforme, (x,y)) # On affiche la plateforme sur la fenetre
				elif sprite == 'p':
					fenetre.blit(portal, (x,y)) # On affiche le portail sur la fenetre
				num_case += 1
			num_ligne += 1

	def onPlateforme(self, x, y):
		onPlateforme = False

		# division entiere pour trouver le bloc dans lequel se trouve le point (x; y)
		blocx = x // taille_plateforme
		blocy = y // taille_plateforme

		# On regarde si un bloc 'm' de trouve a l'emplacement du bloc qui contient (x; y)
		if blocx < len(self.structure[1]) and blocy < len(self.structure) : # On evite l'erreur out of range
			if self.structure[blocy][blocx] == 'm' or self.structure[blocy][blocx] == 'i':
				onPlateforme = True

        # On considere la sortie de la fenetre comme un bloc
		if blocx >= len(self.structure[1]) and blocy >= len(self.structure) :
			onPlateforme = True

		return onPlateforme
