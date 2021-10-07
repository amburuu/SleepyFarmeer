# Constantes du jeu SleepyFarmer
import pygame

from classes import *
# Images du jeu

img_tomate = "assets/fruits&légumes/tomate.png"
img_courgette = "assets/fruits&légumes/courgette.png"
img_mais = "assets/fruits&légumes/mais.png"
img_fraise = "assets/fruits&légumes/fraises.png"
img_plant = "assets/cases_niveaux/herbe_mur.png"
img_background = "assets/divers/fond_champ.png"
img_raven_repos = "assets/piaf2/piaf_droite.png"
img_raven_vol_est = "assets/piaf2/piaf_vol_est.png"
img_raven_vol_ouest = "assets/piaf2/piaf_vol_ouest.png"
img_raven_vol_nord = "assets/piaf2/piaf_vol_nord.png"
img_raven_vol_sud = "assets/piaf2/piaf_vol_sud.png"
img_raven_vol_sud_est = "assets/piaf2/piaf_vol_sud_est.png"
img_raven_vol_sud_ouest = "assets/piaf2/piaf_vol_sud_ouest.png"
img_raven_nord_est = "assets/piaf2/piaf_vol_nord_est.png"
img_raven_nord_ouest = "assets/piaf2/piaf_vol_nord_ouest.png"
img_raven_alerte_droite = "assets/piaf/piaf_alerte_droite.png"
img_raven_alerte_gauche = "assets/piaf/piaf_alerte_gauche.png"
img_farmer_dors = "assets/pépé/pépé_ronfle.png"
img_farmer_reveille = "assets/pépé/pépé_surpris.png"
img_perso_triste = "assets/enfant/triste.png"
img_perso_happy = "assets/enfant/heureux.png"
img_perso_right = "assets/enfant/enfant_droite.png"
img_perso_left = "assets/enfant/enfant_gauche.png"
img_perso_up = "assets/enfant/enfant_dos.png"
img_perso_down = "assets/enfant/enfant_face.png"
img_epouv = "assets/epouvantail/scarecrow.png"
img_home = "assets/divers/menu_accueil.png"
img_gameover = "assets/divers/game_over.png"
img_vie_pleine = "assets/vie/coeur_plein.png"
img_vie_vide = "assets/vie/coeur_vide.png"
img_etale = "assets/divers/etale_fruits_leg.png"
img_bouton_on = "assets/divers/son_on.png"
img_bouton_off = "assets/divers/son_off.png"
img_bouton_credit = "assets/divers/bouton_info.png"
img_credit = "assets/divers/credits.png"
img_victory = "assets/divers/victoire.png"
img_logo = "assets/divers/sleepy_farmer_logo.png"
img_cpt = "assets/divers/compteur.png"

cpt_list = []
cpt_list.append('assets/divers/0.png')
cpt_list.append('assets/divers/1.png')
cpt_list.append('assets/divers/2.png')
cpt_list.append('assets/divers/3.png')
cpt_list.append('assets/divers/4.png')

# Paramètre du jeu
nb_cases_hauteur = 12
nb_cases_largeur = 16
taille_case = 64
map_hauteur = nb_cases_hauteur*taille_case
map_largeur = nb_cases_largeur*taille_case
run_main = True
home = True
game = False
gameover = False
bool_son = True
credit = False

#liste des fichiers niveau
liste_niveaux = []
liste_niveaux.append('assets/niveaux/map')
liste_niveaux.append('assets/niveaux/map2')
liste_niveaux.append('assets/niveaux/map3')
liste_niveaux.append('assets/niveaux/map4')
liste_niveaux.append('assets/niveaux/map5')

#liste des dialogues
liste_dialogues = []
liste_dialogues.append('assets/dialogues/nous_ronpichames.png')
liste_dialogues.append('assets/dialogues/le_fermier_dort.png')
liste_dialogues.append('assets/dialogues/attention_au_corbeau.png')
liste_dialogues.append('assets/dialogues/corbeau_balance.png')
liste_dialogues.append('assets/dialogues/vioc_enerve.png')
liste_dialogues.append('assets/dialogues/oh_non_repere.png')
liste_dialogues.append('assets/dialogues/bravo_gagne.png')
liste_dialogues.append('assets/dialogues/papy_balance_aux_darons.png')

#var
liste_random = [0, 1, 2, 3, 4]
cpt1 = 0
cpt2 = 0
cpt_vie = 3
cpt_fruit = 0
difficulty = 0

#liste des boutons

#bouton jouer - accueil
bouton_play = pygame.image.load("assets/divers/jouer.png")
bouton_play_rect = bouton_play.get_rect()
bouton_play_rect.x = 255
bouton_play_rect.y = 374

# bouton recommencer - gameover
bouton_replay = pygame.image.load("assets/divers/recommencer.png")
bouton_replay_rect = bouton_play.get_rect()
bouton_replay_rect.x = 255
bouton_replay_rect.y = 546

# bouton son - game
bouton_sound = pygame.image.load(img_bouton_off)
bouton_sound_rect = bouton_sound.get_rect()
bouton_sound_rect.x = 0
bouton_sound_rect.y = 11*taille_case

#bouton credit - jeu
bouton_credit_game = pygame.image.load(img_bouton_credit)
bouton_credit_game_rect = bouton_credit_game.get_rect()
bouton_credit_game_rect.x = 1*taille_case
bouton_credit_game_rect.y = 11*taille_case

#bouton credit - home
bouton_credit_home = pygame.image.load("assets/divers/boutons_credits.png")
bouton_credit_home_rect = bouton_credit_home.get_rect()
bouton_credit_home_rect.x = 255
bouton_credit_home_rect.y = 505

#liste des sons

# nom (keys) des objets son
bruit_pas_sound = "bruit_pas_sound"
corbeau_sound = "corbeau_sound"
gameover_sound = "gameover_sound"
musique_accueil_sound = "musique_accueil_sound"
musique_fond_sound = "musique_fond_sound"
angry_farmer_sound = "angry_farmer_sound"
ramasse_sound = "ramasse_sound"
repere_sound = "repere_sound"
victoire_sound = "victoire_sound"

# declaration des chemin d'acces (values)
son_bruits_pas = "assets/sounds/bruits_pas.wav"
son_corbeau = "assets/sounds/corbeau.wav"
son_gameover = "assets/sounds/game_over.wav"
son_musique_home = "assets/sounds/musique_accueil.mp3"
son_musique_fond = "assets/sounds/musique_fond.wav"
son_angry_farmer = "assets/sounds/pepe_grogne.wav"
son_ramasse = "assets/sounds/ramasse.wav"
son_repere = "assets/sounds/repere.wav"
son_victoire = "assets/sounds/victoire.wav"


