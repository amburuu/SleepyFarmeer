import pygame
from pygame.locals import *

from classes import *
from constantes import *
from time import *
from random import *
from math import *

pygame.init()

# 144 cases de jeu | résolution 1024*768
window = pygame.display.set_mode((map_largeur, map_hauteur))
# Titre du jeu
pygame.display.set_caption("SleepyFarmer")
#SoundManager
son_manager = SoundManager()

def afficheCredits(window):
    credits = pygame.image.load(img_credit).convert()
    window.blit(credits, (0, 0))
    pygame.display.flip()
    sleep(5)

def affiche(window):
    vie1 = pygame.image.load(img_vie_pleine).convert_alpha()
    vie2 = pygame.image.load(img_vie_pleine).convert_alpha()
    vie3 = pygame.image.load(img_vie_pleine).convert_alpha()
    #affichage etale de fruit&legumes et logo
    etale = pygame.image.load(img_etale).convert_alpha()
    logo = pygame.image.load(img_logo).convert_alpha()
    compteur = pygame.image.load(img_cpt).convert_alpha()
    increment = pygame.image.load(cpt_list[cpt_fruit]).convert_alpha()
    button_info = pygame.image.load(img_bouton_credit).convert_alpha()

    if bool_son == False:
        bouton_son = pygame.image.load(img_bouton_off).convert_alpha()

    else:
        bouton_son = pygame.image.load(img_bouton_on).convert_alpha()

    #affichage des vies
    if cpt_vie == 3:
        window.blit(vie1, (0, 0))
        window.blit(vie2, (taille_case, 0))
        window.blit(vie3, (taille_case*2, 0))


    elif cpt_vie == 2:
        vie3 = pygame.image.load(img_vie_vide).convert_alpha()
        window.blit(vie1, (0, 0))
        window.blit(vie2, (taille_case, 0))
        window.blit(vie3, (taille_case * 2, 0))


    elif cpt_vie == 1:
        vie3 = pygame.image.load(img_vie_vide).convert_alpha()
        vie2 = pygame.image.load(img_vie_vide).convert_alpha()
        window.blit(vie1, (0, 0))
        window.blit(vie2, (taille_case, 0))
        window.blit(vie3, (taille_case * 2, 0))


    elif cpt_vie == 0:
        vie3 = pygame.image.load(img_vie_vide).convert_alpha()
        vie2 = pygame.image.load(img_vie_vide).convert_alpha()
        vie1 = pygame.image.load(img_vie_vide).convert_alpha()
        window.blit(vie1, (0, 0))
        window.blit(vie2, (taille_case, 0))
        window.blit(vie3, (taille_case * 2, 0))


    window.blit(bouton_son, (0, 11*taille_case))
    window.blit(bouton_credit_game, (1*taille_case, 11*taille_case))
    window.blit(etale, (0, 6*taille_case))
    window.blit(logo, (0, 1 * taille_case))
    window.blit(compteur, (0, 9*taille_case))
    window.blit(increment, (taille_case, 9 * taille_case + 44))

def dialogue(num):
    pygame.mixer.music.pause()
    sleep(3)
    #intro
    if num == 0:
        for i in range(3):
            affiche = pygame.image.load(liste_dialogues[num]).convert_alpha()
            window.blit(affiche, (0,0))
            pygame.display.flip()
            if num == 2:
                son_manager.play(corbeau_sound)

            pygame.time.wait(3000)
            num += 1

    #detection
    elif num == 3:
        for j in range(3):
            affiche = pygame.image.load(liste_dialogues[num]).convert_alpha()
            window.blit(affiche, (0,0))
            pygame.display.flip()

            if num == 3:
                son_manager.play(repere_sound)

            elif num == 4:
                son_manager.play(angry_farmer_sound)

            pygame.time.wait(3000)
            num += 1

    #congratulation
    elif num == 6:
        affiche = pygame.image.load(liste_dialogues[num]).convert_alpha()
        window.blit(affiche, (0, 0))
        pygame.display.flip()
        son_manager.play(victoire_sound)
        pygame.time.wait(4000)

    #papy balance aux parents
    elif num == 7:
        affiche = pygame.image.load(liste_dialogues[num-4]).convert_alpha()
        window.blit(affiche, (0,0))
        pygame.display.flip()
        son_manager.play(repere_sound)
        pygame.time.wait(3000)

        affiche = pygame.image.load(liste_dialogues[num]).convert_alpha()
        window.blit(affiche, (0, 0))
        pygame.display.flip()
        son_manager.play(angry_farmer_sound)
        pygame.time.wait(3000)

    pygame.mixer.music.play(-1, 0.0)

# Boucle principale
while run_main:

    pygame.display.flip()
    pygame.time.Clock().tick(30)
    son_manager.load(True)
    # Boucle ecran d'accueil
    while home:
        pygame.display.flip()
        pygame.time.Clock().tick(30)

        accueil = pygame.image.load(img_home).convert()
        window.blit(accueil, (0, 0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                home = False
                run_main = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_play_rect.collidepoint(event.pos):
                    home = False
                    game = True

                #bouton credit
                elif bouton_credit_home_rect.collidepoint(event.pos):
                    afficheCredits(window)

    # Boucle du jeu
    while game:
        pygame.display.flip()
        pygame.time.Clock().tick(30)

        # on eteint le son d'accueil, play le son du jeu - cf def load()
        son_manager.load(False)
        #pygame.time.wait(100)
        background = pygame.image.load(img_background).convert()
        window.blit(background, (0, 0))

        farmer = pygame.image.load(img_farmer_dors).convert_alpha()
        window.blit(farmer, (1 * taille_case, 4 * taille_case))

        affiche(window)

        level = Level(liste_niveaux[difficulty])
        level.generate()

        if difficulty == 0:
            dialogue(0)

        # Calcul des coordonnées des epouvantails du niveau et stockage dans liste coord_epouv [y,x]
        coord_epouv1 = []
        for coordy in range(12):
            for coordx in range(16):
                if level.structure[coordy][coordx] == 'e':
                    coord = []
                    coord.append(coordy * taille_case)
                    coord.append(coordx * taille_case)
                    coord_epouv1.append(coord)

        # on evite la division par 0
        liste_random.remove(4)
        rand1 = choice(liste_random)
        liste_random.append(4)

        liste_random.remove(3)
        rand2 = choice(liste_random)
        liste_random.append(3)

        #instanciation des objets moteurs
        chenapan = Perso(img_perso_right, img_perso_left, img_perso_up, img_perso_down, level)
        corbeau1 = Crow(img_raven_vol_est, img_raven_vol_ouest, img_raven_vol_nord, img_raven_vol_sud, img_raven_nord_est, img_raven_nord_ouest, img_raven_vol_sud_est, img_raven_vol_sud_ouest, level, coord_epouv1[4][1], coord_epouv1[4][0])
        corbeau2 = Crow(img_raven_vol_est, img_raven_vol_ouest, img_raven_vol_nord, img_raven_vol_sud, img_raven_nord_est, img_raven_nord_ouest, img_raven_vol_sud_est, img_raven_vol_sud_ouest, level, coord_epouv1[3][1], coord_epouv1[3][0])

        if coord_epouv1[rand2][1] == corbeau2.x:
            coef2 = 0
        else:
            coef2 = (coord_epouv1[rand2][0] - corbeau2.y) / (coord_epouv1[rand2][1] - corbeau2.x)
            coef2 = abs(coef2)

        if coord_epouv1[rand1][1] == corbeau1.x:
            coef1 = 0
        else:
            coef1 = (coord_epouv1[rand1][0] - corbeau1.y) / (coord_epouv1[rand1][1] - corbeau1.x)
            coef1 = abs(coef1)
        # Ydest - Ydep / Xdest - Xdep = Coefficient directeur
        #valeur absolu du coef

        continu = True

        while continu:
            pygame.time.Clock().tick(30)

            cpt1 += 1

            if difficulty > 2:
                cpt2 += 1

            for event in pygame.event.get():
                if event.type == QUIT:
                    game = False
                    continu = False
                    run_main = False
                    pygame.quit()

                elif event.type == KEYDOWN:
                    # Si l'utilisateur presse Echap ici, on revient seulement au depart
                    if event.key == K_ESCAPE:
                        continu = False
                    # Touches de déplacement
                    elif event.key == K_RIGHT:
                        chenapan.deplacer('right', son_manager)
                    elif event.key == K_LEFT:
                        chenapan.deplacer('left', son_manager)
                    elif event.key == K_UP:
                        chenapan.deplacer('up', son_manager)
                    elif event.key == K_DOWN:
                        chenapan.deplacer('down', son_manager)

                elif event.type == MOUSEBUTTONDOWN:
                    #bouton son ON/OFF
                    if bouton_sound_rect.collidepoint(event.pos):
                        bool_son = not bool_son
                        if bool_son == True:
                            pygame.mixer.music.play(-1, 0.0)
                        else:
                            pygame.mixer.music.pause()

                    elif bouton_credit_game_rect.collidepoint(event.pos):
                        afficheCredits(window)

            window.blit(background, (0, 0))

            level.display(window)
            affiche(window)
            window.blit(chenapan.direction, (chenapan.x, chenapan.y))

            corbeau1.deplacer(coord_epouv1[rand1][1], coord_epouv1[rand1][0], coef1, difficulty)
            window.blit(corbeau1.direction, (corbeau1.x - 96, corbeau1.y - 96))

            window.blit(farmer, (1 * taille_case, 4 * taille_case))


            if difficulty > 2:
                corbeau2.deplacer(coord_epouv1[rand2][1], coord_epouv1[rand2][0], coef2, difficulty)
                window.blit(corbeau2.direction, (corbeau2.x - 96, corbeau2.y - 96))


            pygame.display.flip()

            save1 = rand1

            # troncature : on garde seulement la partie entiere des coordonnées de corbeau1 : methode floor()
            # test : si coord epouv == corbeau1 on change de direction
            # Dû a la troncature, on vérifie si les coordonées sont bornées entre +1 ET -1 pixel
            if ((floor(corbeau1.y) <= coord_epouv1[rand1][0] + 1) and (floor(corbeau1.y) >= coord_epouv1[rand1][0] - 1)) \
                    and ((floor(corbeau1.x) <= coord_epouv1[rand1][1] + 1) and (floor(corbeau1.x) >= coord_epouv1[rand1][1] - 1)):

                # On mets le coef a 0 pour eviter le tremblement
                coef1 = 0
                # temps d'attente du corbeau sur l'epouvantail
                if cpt1 >= 100:

                    liste_random.remove(save1)
                    rand1 = choice(liste_random)
                    liste_random = [0, 1, 2, 3, 4]

                    # Ydest - Ydep / Xdest - Xdep = Coefficient directeur
                    if coord_epouv1[rand1][1] == corbeau1.x:
                        coef1 = 0
                    else:
                        coef1 = (coord_epouv1[rand1][0] - corbeau1.y) / (coord_epouv1[rand1][1] - corbeau1.x)
                        coef1 = abs(coef1)
                    cpt1 = 0

            if difficulty > 2:
                save2 = rand2

                # troncature : on garde seulement la partie entiere des coordonnées de corbeau1 : methode floor()
                # test : si coord epouv == corbeau1 on change de direction
                # Dû a la troncature, on vérifie si les coordonées sont bornées entre +1 ET -1 pixel
                if ((floor(corbeau2.y) <= coord_epouv1[rand2][0] + 1) and (floor(corbeau2.y) >= coord_epouv1[rand2][0] - 1))\
                        and ((floor(corbeau2.x) <= coord_epouv1[rand2][1] + 1) and (floor(corbeau2.x) >= coord_epouv1[rand2][1] - 1)):

                    # On mets le coef a 0 pour eviter le tremblement
                    coef2 = 0
                    #temps d'attente du corbeau sur l'epouvantail
                    if cpt2 >= 75:

                        liste_random.remove(save2)
                        rand2 = choice(liste_random)
                        liste_random = [0, 1, 2, 3, 4]

                        # Ydest - Ydep / Xdest - Xdep = Coefficient directeur
                        if coord_epouv1[rand2][1] == corbeau2.x:
                            coef2 = 0
                        else:
                            coef2 = (coord_epouv1[rand2][0] - corbeau2.y) / (coord_epouv1[rand2][1] - corbeau2.x)
                            coef2 = abs(coef2)

                        cpt2 = 0

            # si le joueur est detecte
            if corbeau1.detection(chenapan.x, chenapan.y) == True or (
                difficulty > 2 and corbeau2.detection(chenapan.x, chenapan.y)) == True:

                chenapan.direction = pygame.image.load(img_perso_triste).convert_alpha()
                corbeau1.direction = pygame.image.load(img_raven_alerte_droite).convert_alpha()
                farmer = pygame.image.load(img_farmer_reveille).convert_alpha()

                window.blit(background, (0, 0))

                level.display(window)
                affiche(window)
                window.blit(chenapan.direction, (chenapan.x, chenapan.y))

                window.blit(corbeau1.direction, (corbeau1.x - 96, corbeau1.y - 96))

                if difficulty > 2:
                    corbeau2.direction = pygame.image.load(img_raven_alerte_droite).convert_alpha()
                    window.blit(corbeau2.direction, (corbeau2.x - 96, corbeau2.y - 96))

                window.blit(farmer, (1 * taille_case, 4 * taille_case))

                pygame.display.flip()

                cpt_vie -= 1
                if cpt_vie == 0:
                    dialogue(7)
                else:
                    dialogue(3)

                chenapan.direction = chenapan.right
                corbeau1.direction = corbeau1.est
                corbeau2.direction = corbeau2.est
                farmer = pygame.image.load(img_farmer_dors).convert_alpha()

                chenapan.case_x = nb_cases_largeur - nb_cases_hauteur
                chenapan.case_y = 0
                chenapan.x = chenapan.case_x * taille_case
                chenapan.y = 0

            pygame.display.flip()

            # Si le joueur mange un fruit on incremente
            if level.structure[chenapan.case_y][chenapan.case_x] == 'f' or level.structure[chenapan.case_y][chenapan.case_x] == 'm' or level.structure[chenapan.case_y][chenapan.case_x] == 't' or level.structure[chenapan.case_y][chenapan.case_x] == 'c':
                cpt_fruit += 1
                son_manager.play(ramasse_sound)
                level.rm_fruit(chenapan.case_x, chenapan.case_y)

            # Si le joueur a mangé tout les fruits alors on change de niveau
            elif cpt_fruit == 4:

                chenapan.direction = pygame.image.load(img_perso_happy).convert_alpha()
                window.blit(chenapan.direction, (chenapan.x, chenapan.y))

                dialogue(6)
                continu = False
                difficulty += 1
                cpt_fruit = 0

            if difficulty > 4:
                continu = False
                game = False
                gameover = True

            # Si on a plus de vie alors le jeu est fini : gameover
            if cpt_vie == 0:
                pygame.mixer.music.stop()
                son_manager.play(gameover_sound)
                continu = False
                game = False
                gameover = True


    while gameover:
        pygame.display.flip()
        pygame.time.Clock().tick(30)

        if difficulty > 4:
            victory = pygame.image.load(img_victory).convert()
            window.blit(victory, (0, 0))
        else:
            game_over = pygame.image.load(img_gameover).convert()
            window.blit(game_over, (0,0))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                home = False
                run_main = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if bouton_replay_rect.collidepoint(event.pos):
                    difficulty = 0
                    cpt_vie = 3
                    cpt_fruit = 0
                    gameover = False
                    game = True
