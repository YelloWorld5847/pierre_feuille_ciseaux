import time
import pygame
import random
from game import Game

pygame.init()

# définir une clock
clock = pygame.time.Clock()

FPS = 30
OCCURRENCE = 15

BACKGROUND = (255, 255, 255)
MAP_SIZE = 700
PAD_X = 50
PAD_Y = 50

screen_width = MAP_SIZE + PAD_X * 2
screen_height = MAP_SIZE + PAD_Y * 2
center_x = screen_width / 2
center_y = screen_height / 2

objets = {
    'ciseaux': {'size_spawn': 30, 'num': 200, 'kill': ['feuille'], 'img': r'assets/ciseaux_50x50.png'},
    'feuille': {'size_spawn': 30, 'num': 200, 'kill': ['pierre'], 'img': r'assets/papier_50x67.png'},
    'pierre': {'size_spawn': 30, 'num': 200, 'kill': ['ciseaux'], 'img': r'assets/pierre_50x50.png'},
}


# générer la fenêtre du jeu
pygame.display.set_caption('pierre_feuille_ciseaux')
screen = pygame.display.set_mode((screen_width, screen_height))


game = Game(screen_width, screen_height, OCCURRENCE, MAP_SIZE, PAD_X, PAD_Y, center_x, center_y)



game.creat_all_obj(objets)

running = True

while running:
    # appliquer l'arrière plan au jeu
    screen.fill(BACKGROUND)

    # Mettre à jour la position de tous les objets
    for objet in game.objets:
        objet.update_position()  # Mettre à jour chaque objet

    # Vérifier les collisions
    game.check_collisions()

    for objet in game.objets:
        objet.rebondir_bords()  # Vérifier si chaque objet doit rebondir
        screen.blit(objet.image, objet.rect)  # Dessiner chaque objet sur l'écran

    # Mettre à jour l'affichage
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print('Fermeture du jeu')

    # fixé le nombre de FPS sur le clock
    clock.tick(FPS)
