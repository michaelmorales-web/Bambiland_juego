import pygame
import random

class Manzana():

    def __init__(self):

        self.sprite = pygame.image.load(
            "assets/images/manzana.gif"
        ).convert_alpha()

        self.rect = self.sprite.get_rect()

        self.reubicar()

    def reubicar(self):

        self.x = random.randint(100, 900)
        self.y = random.randint(150, 700)

        self.rect.x = self.x
        self.rect.y = self.y