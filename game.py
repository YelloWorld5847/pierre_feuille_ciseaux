import pygame
from objet import Objet
from sounds import SoundManager
import math

class Game:
    def __init__(self, screen_width, screen_height, OCCURRENCE, MAP_SIZE, PAD_X, PAD_Y, center_x, center_y):  # Ajouter un paramètre pour le nombre d'objets
        self.sound_manager = SoundManager()

        self.same_size = True
        self.OCCURRENCE = OCCURRENCE
        self.MAP_SIZE = MAP_SIZE
        self.PAD_X = PAD_X
        self.PAD_Y = PAD_Y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.center_x = center_x
        self.center_y = center_y
        self.list_objets = {}


        self.presse = {}

    def calculate_object_size(self, window_width, window_height, num_objects, size_factor=0.4):
        if num_objects > 150:
            size_factor = num_objects / 400

        # print(f'facteur de réduction : {size_factor}')

        # Choisir un nombre de colonnes basé sur la racine carrée du nombre d'objets pour une distribution équilibrée
        cols = int(math.ceil(math.sqrt(num_objects)))
        rows = int(math.ceil(num_objects / cols))

        # Calculer la taille maximale d'un objet en fonction de la taille de la fenêtre
        object_width = window_width / cols
        object_height = window_height / rows

        # Retourner la taille de l'objet comme la plus petite dimension
        return min(object_width, object_height)  * size_factor

    def creat_all_obj(self, objets):
        NUM_OF_OBJ = len(objets)

        first = True


        # Distance parcourue le long du périmètre
        distance_traveled = 0
        # calculer la taille de l'objet en fonction de l'espace de jeu
        size_objet = []

        # Parcours des côtés du carré
        for key, value in objets.items():
            print(f'key= {key} ; value = {value}')

            if not self.same_size:
                # calculer la taille de l'objet en fonction de l'espace de jeu
                size_objet = self.calculate_object_size(self.MAP_SIZE, self.MAP_SIZE, value['num'] * NUM_OF_OBJ)

            if first:
                if self.same_size:
                    # calculer la taille de l'objet en fonction de l'espace de jeu
                    size_objet = self.calculate_object_size(self.MAP_SIZE, self.MAP_SIZE, value['num'] * NUM_OF_OBJ)

                # 1. `value['size_spawn']`: la taille de l'espace où ils ponrront spawn
                # 2. `size_objet` la taille de l'objet
                # 3. ajout d'une petite valeur pour evité que ce soi collé et qu'il ne puisse plus bougé
                spawn_pad = value['size_spawn'] * 2 + size_objet + 5  # petite marge en plus pour pas

                L = self.MAP_SIZE - (spawn_pad * 2)

                # Calcul du périmètre du carré
                perimeter = L * 4
                # Calcul de la distance entre chaque élément
                d = perimeter / NUM_OF_OBJ

                start_x, start_y = self.PAD_X + spawn_pad, self.PAD_Y + spawn_pad  # Coordonnées du coin supérieur gauche du carré
                # Commencer à la position du coin supérieur gauche
                current_x, current_y = start_x, start_y
                self.creat_new_obj(key, value, current_x, current_y, size_objet)
                first = False
                continue

            distance_traveled += d  # Avancer de d unités

            # Vérifier sur quel côté on se trouve et ajuster les coordonnées
            if distance_traveled <= L:  # 1er côté (de gauche à droite)
                current_x = start_x + distance_traveled
                current_y = start_y
            elif distance_traveled <= 2 * L:  # 2ème côté (de haut en bas)
                current_x = start_x + L
                current_y = start_y + (distance_traveled - L)
            elif distance_traveled <= 3 * L:  # 3ème côté (de droite à gauche)
                current_x = start_x + L - (distance_traveled - 2 * L)
                current_y = start_y + L
            else:  # 4ème côté (de bas en haut)
                current_x = start_x
                current_y = start_y + L - (distance_traveled - 3 * L)

            # Ajouter un nouvel objet avec les positions calculées
            self.creat_new_obj(key, value, current_x, current_y, size_objet)

        self.num_type = len(self.list_objets)
        self.objets = pygame.sprite.Group()  # Créer un groupe pour les objets
        for key, value in self.list_objets.items():
            for _ in range(value['num']):  # Créer plusieurs objets
                objet_ = Objet(key, value, self.num_type, self.MAP_SIZE, self.PAD_X, self. PAD_Y)
                self.objets.add(objet_)  # Ajouter chaque objet au groupe


    def creat_new_obj(self, name, objet, x, y, size):
        print(objet)
        self.list_objets[name] = objet | {'x': int(x), 'y': int(y), 'size': size}
        # self.list_objets[name] +=
        # print(self.list_objets)
    def check_collisions(self):
        # Vérifier les collisions entre tous les objets du groupe
        for objet in self.objets:
            # Récupérer la liste des objets avec lesquels il y a collision
            collisions = pygame.sprite.spritecollide(objet, self.objets, False)
            collisions.remove(objet)  # Retirer l'objet lui-même de la liste des collisions
            # objet = le tueur
            # kill = l'objet que le tueur a le droit de tuer
            # other_obj = celui que le tueur veux tuer
            if collisions:
                for other_obj in collisions:
                    # ciseaux entre en collision avec feuille
                    # kill de pierre : ciseaux == ciseaux ?
                    for kill in objet.objet_dict['kill']:
                        # print(f'{objet.name} veut kill {other_obj.name}. kill de {objet.name} : {kill}   {kill == other_obj.name}')
                        if kill == other_obj.name:
                            # print(f'--Kill Réussie--  {objet.img}')
                            # print(f'obj = {objet.name}  auther obj = {other_obj.name}')
                            self.sound_manager.play(f'{objet.name}_kill_{other_obj.name}')
                            other_obj.reset(objet.name, objet.objet_dict)



