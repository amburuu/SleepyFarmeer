import pygame
import math

from pygame.locals import *
from constantes import *
from math import *

class SoundManager:

    #dictionaire des sons = map<K, V>
    def __init__(self):
        self.sounds = {
            bruit_pas_sound : pygame.mixer.Sound(son_bruits_pas),
            corbeau_sound : pygame.mixer.Sound(son_corbeau),
            gameover_sound : pygame.mixer.Sound(son_gameover),
            musique_accueil_sound : pygame.mixer.Sound(son_musique_home),
            musique_fond_sound : pygame.mixer.Sound(son_musique_fond),
            angry_farmer_sound : pygame.mixer.Sound(son_angry_farmer),
            ramasse_sound : pygame.mixer.Sound(son_ramasse),
            repere_sound : pygame.mixer.Sound(son_repere),
            victoire_sound : pygame.mixer.Sound(son_victoire),
        }

    def play(self, name):
        self.sounds[name].play()

    def load(self, bool):
        if bool == True:
            pygame.mixer.music.load(son_musique_home)
            pygame.mixer.music.play(-1, 0.0)

        else:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(son_musique_fond)
            pygame.mixer.music.play(-1, 0.0)

class Level:
    # Classe de création d'un level de jeu
    def __init__(self, file):
        self.file = file
        self.structure = 0

    def generate(self):
        # On instancie les listes du quadrillage à partir du fichier du level
        with open(self.file, "r") as file:
            level_structure = []
            for line in file:
                level_line = []
                for case in line:
                    if case != '\n':
                        level_line.append(case)
                level_structure.append(level_line)
            self.structure = level_structure

    def display(self, window):
        # Méthode d'affichage des composants precédemment générés
        plant = pygame.image.load(img_plant).convert_alpha()
        scarecrow = pygame.image.load(img_epouv).convert_alpha()
        # On parcourt les données du level
        line_number = 0
        for line in self.structure:
            line_case = 0
            for case in line:
                x = line_case*taille_case
                y = line_number*taille_case
                if case == 'p': #p = plant
                    window.blit(plant, (x,y))

                elif case == 'f': #f fruit
                    fruit = pygame.image.load(img_fraise).convert_alpha()
                    window.blit(fruit, (x,y))

                elif case == 't': #t tomate
                    fruit = pygame.image.load(img_tomate).convert_alpha()
                    window.blit(fruit, (x,y))

                elif case == 'c': #c courgette
                    fruit = pygame.image.load(img_courgette).convert_alpha()
                    window.blit(fruit, (x,y))

                elif case == 'm': #m mais
                    fruit = pygame.image.load(img_mais).convert_alpha()
                    window.blit(fruit, (x,y))

                elif case == 'e': #e epouvantail
                    window.blit(scarecrow, (x,y))

                line_case += 1
            line_number += 1

    def rm_fruit(self, x, y):
        self.structure[y][x] = '0'

class Perso:
    
    def __init__(self, right, left, up, down, level):
        # Sprites du personnage

        self.right = pygame.image.load(right).convert_alpha()
        self.left = pygame.image.load(left).convert_alpha()
        self.up = pygame.image.load(up).convert_alpha()
        self.down = pygame.image.load(down).convert_alpha()
        # Position du personnage en cases et en pixels
        self.case_x = nb_cases_largeur-nb_cases_hauteur
        self.case_y = 0
        self.x = self.case_x*taille_case
        self.y = 0
        # Direction par défaut
        self.direction = self.right
        # level dans lequel le personnage se trouve 
        self.level = level


    def deplacer(self, direction, son_manager):

        # Déplacement vers la droite
        if direction == 'right':
            # Pour ne pas dépasser l'écran
            if self.case_x < (nb_cases_largeur - 1):
                # On vérifie que la case de destination n'est pas un mur
                if self.level.structure[self.case_y][self.case_x + 1] != 'p' and self.level.structure[self.case_y][self.case_x + 1] != 'e':
                    # Déplacement d'une case
                    self.case_x += 1
                    # Calcul de la position "réelle" en pixel
                    self.x = self.case_x * taille_case
            # Image dans la bonne direction
            self.direction = self.right

        # Déplacement vers la gauche
        if direction == 'left':
            if self.case_x > nb_cases_largeur-nb_cases_hauteur:
                if self.level.structure[self.case_y][self.case_x - 1] != 'p' and self.level.structure[self.case_y][self.case_x - 1] != 'e':
                    self.case_x -= 1
                    self.x = self.case_x * taille_case
            self.direction = self.left

        # Déplacement vers le haut
        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y - 1][self.case_x] != 'p' and self.level.structure[self.case_y - 1][self.case_x] != 'e':
                    self.case_y -= 1
                    self.y = self.case_y * taille_case
            self.direction = self.up

        # Déplacement vers le bas
        if direction == 'down':
            if self.case_y < (nb_cases_hauteur - 1):
                if self.level.structure[self.case_y + 1][self.case_x] != 'p' and self.level.structure[self.case_y + 1][self.case_x] != 'e':
                    self.case_y += 1
                    self.y = self.case_y * taille_case
            self.direction = self.down

        # son des pas
        son_manager.play(bruit_pas_sound)

class Crow:

    def __init__(self, est, ouest, nord, sud, nordest, nordouest, sudest, sudouest, level, x_dep, y_dep):
        self.est = pygame.image.load(est).convert_alpha()
        self.ouest = pygame.image.load(ouest).convert_alpha()
        self.nord = pygame.image.load(nord).convert_alpha()
        self.sud  = pygame.image.load(sud).convert_alpha()
        self.nordest = pygame.image.load(nordest).convert_alpha()
        self.nordouest = pygame.image.load(nordouest).convert_alpha()
        self.sudouest = pygame.image.load(sudouest).convert_alpha()
        self.sudest = pygame.image.load(sudest).convert_alpha()
        self.x = x_dep
        self.y = y_dep
        self.direction = self.est
        self.level = level

    def deplacer(self, x_epouv, y_epouv, coef, difficulty):

        pw = math.pow(2, difficulty+1)

        if x_epouv > self.x:
            if y_epouv > self.y:
                self.x += pw
                self.y = self.y + pw*coef
                #sud-est
                self.direction = self.sudest
            elif y_epouv == floor(self.y) or y_epouv -1 == floor(self.y) or y_epouv + 1 == floor(self.y):
                self.x += pw
                #est
                self.direction = self.est
            else:
                self.x += pw
                self.y = self.y - pw*coef
                #nord est
                self.direction = self.nordest

        elif x_epouv < self.x:
            if y_epouv > self.y:
                self.x -= pw
                self.y = self.y + pw*coef
                #sud ouest
                self.direction = self.sudouest
            elif y_epouv == floor(self.y) or y_epouv -1 == floor(self.y) or y_epouv + 1 == floor(self.y):
                self.x -= pw
                #ouest
                self.direction = self.ouest
            else:
                self.x -= pw
                self.y = self.y - pw*coef
                #nord ouest
                self.direction = self.nordouest

        elif x_epouv == self.x:

            if coef == 0:
                self.direction = pygame.image.load(img_raven_repos).convert_alpha()
            else:
                if y_epouv > self.y:
                    self.y = self.y + pw*coef
                    #sud
                    self.direction = self.sud
                else:
                    self.y = self.y - pw*coef
                    #nord
                    self.direction = self.nord

    def detection(self, x_perso, y_perso):

        if ((x_perso - self.x)*(x_perso - self.x)) + ((y_perso - self.y)*(y_perso - self.y)) <= 16384:
            return True
        else:
            return False

