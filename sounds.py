import pygame
from playsound import playsound

class SoundManager:

    def __init__(self):

        self.sounds = {
            'ciseaux_kill_feuille': pygame.mixer.Sound('assets/sounds/02-cut_rogner.mp3'),
            'feuille_kill_pierre': pygame.mixer.Sound('assets/sounds/01_feuill_pierre.wav'),
            'pierre_kill_ciseaux': pygame.mixer.Sound('assets/sounds/01_pierre_ciseaux.wav'),
        }

    def play(self, name):
        self.sounds[name].play()