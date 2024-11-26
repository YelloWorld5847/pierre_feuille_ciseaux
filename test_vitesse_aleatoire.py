import pygame
import random
import math

# Initialisation de pygame
pygame.init()

# Dimensions de la fenêtre
width, height = 800, 600
window = pygame.display.set_mode((width, height))

# Couleurs
WHITE = (255, 255, 255)
RED = (255, 0, 0)


# Classe pour l'élément en mouvement
class MovingObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        # Angle aléatoire en radians (entre 0 et 2π)
        self.angle = random.uniform(0, 2 * math.pi)
        # Vitesse aléatoire entre 0.1 et 5 (par exemple)
        self.speed = 1# random.uniform(0.1, 5)
        self.frame_counter = 0  # Compteur de frames pour les petites vitesses

    def move(self):
        # Si la vitesse est très petite, attendre quelques frames avant de bouger
        if self.speed < 1:
            self.frame_counter += 1
            if self.frame_counter < 60 / self.speed:  # Plus petite la vitesse, plus on attend
                return
            self.frame_counter = 0

        # Calculer le déplacement
        dx = math.cos(self.angle) * self.speed
        dy = math.sin(self.angle) * self.speed

        # Mettre à jour les coordonnées
        self.x += dx
        self.y += dy

        # Gestion des bords de la fenêtre
        if self.x < 0 or self.x > width:
            self.angle = math.pi - self.angle  # Inverser la direction horizontale
        if self.y < 0 or self.y > height:
            self.angle = -self.angle  # Inverser la direction verticale

    def draw(self, surface):
        pygame.draw.circle(surface, RED, (int(self.x), int(self.y)), self.size)


# Création de l'objet
moving_object = MovingObject(width // 2, height // 2)

# Boucle principale
running = True
clock = pygame.time.Clock()

while running:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Remplir l'écran de blanc
    window.fill(WHITE)

    # Déplacer et dessiner l'objet
    moving_object.move()
    moving_object.draw(window)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Limiter la boucle à 60 FPS
    clock.tick(60)

# Quitter pygame
pygame.quit()
