import pygame
import random
import math
from PIL import Image

class Objet(pygame.sprite.Sprite):
    def __init__(self, objet_name, objet_dict, num_type, MAP_SIZE, PAD_X, PAD_Y):
        super().__init__()
        self.num_type = num_type
        self.MAP_SIZE = MAP_SIZE
        self.PAD_X = PAD_X
        self.PAD_Y = PAD_Y
        self.coef_pos = 5
        self.vitesse = random.uniform(3, 5)  # Vitesse aléatoire entre 0.1 et 12

        self.size = int(objet_dict['size'])
        self.sizes = (self.size, self.size)
        
        self.image = self.resize_img(objet_dict['img'], self.sizes)
        self.rect = self.image.get_rect()

        self.reset(objet_name, objet_dict)


        # Calculer la zone où les objets pourront apparaître
        a_x = self.objet_dict['x'] - self.objet_dict['size_spawn']
        b_x = self.objet_dict['x'] + self.objet_dict['size_spawn']
        a_y = self.objet_dict['y'] - self.objet_dict['size_spawn']
        b_y = self.objet_dict['y'] + self.objet_dict['size_spawn']

        if self.name == 'pierre':
            pass

        self.rect.x = round(random.randint(a_x, b_x) / self.coef_pos) * self.coef_pos
        self.rect.y = round(random.randint(a_y, b_y) / self.coef_pos) * self.coef_pos

        # Générer un angle aléatoire entre 0 et 2*PI radians
        angle = random.uniform(0, 2 * math.pi)

        # Déterminer la direction à partir de cet angle (ajusté en floats)
        self.direction_x = math.cos(angle)
        self.direction_y = math.sin(angle)

        # Utiliser des coordonnées flottantes pour plus de précision
        self.float_x = float(self.rect.x)
        self.float_y = float(self.rect.y)

        # Ajout du compteur de frames pour les petites vitesses
        self.frame_counter = 0



    def resize_img(self, image, sizes=(30,30)):

        # Charger et redimensionner l'image avec Pillow
        img = Image.open(image)  # Charger l'image
        img = img.resize(sizes, Image.LANCZOS)  # Redimensionner

        # Convertir l'image Pillow en surface Pygame
        img_surface = pygame.image.fromstring(img.tobytes(), img.size, img.mode)

        return img_surface

    def update_position(self):
        # Si la vitesse est très petite, attendre quelques frames avant de bouger
        if self.vitesse < 1:
            self.frame_counter += 1
            if self.frame_counter < 60 / self.vitesse:  # Plus petite la vitesse, plus on attend
                return
            self.frame_counter = 0

        # Mettre à jour les coordonnées flottantes pour un mouvement fluide
        self.float_x += self.direction_x * self.vitesse
        self.float_y += self.direction_y * self.vitesse

        # Mettre à jour la position du rect en arrondissant les flottants
        self.rect.x = round(self.float_x)
        self.rect.y = round(self.float_y)

    def rebondir_bords(self):
        # Si l'objet touche le bord droit ou gauche, inverser la direction en X
        if self.rect.right >= self.MAP_SIZE + self.PAD_X or self.rect.left <= self.PAD_X:
            self.direction_x *= -1

        # Si l'objet touche le bord supérieur ou inférieur, inverser la direction en Y
        if self.rect.bottom >= self.MAP_SIZE + self.PAD_Y or self.rect.top <= self.PAD_Y:
            self.direction_y *= -1

    def reset(self, objet_name, objet_dict):
        self.name = objet_name
        self.objet_dict = objet_dict
        self.image = self.resize_img(self.objet_dict['img'], self.sizes)
        self.rect = self.image.get_rect(center=self.rect.center)  # Centrer la nouvelle image


"""

"""