import pygame
import random

class Manzana():

    def __init__(self):

        self.sprite = pygame.image.load(
            "assets/images/manzana.gif"
        ).convert_alpha()

        self.rect = self.sprite.get_rect()

    def reubicar(self, fondo):

        while True:

            self.x = random.randint(100, 900)
            self.y = random.randint(150, 700)

            self.rect.x = self.x
            self.rect.y = self.y

            margen = 8

            puntos = [
    (self.rect.left - margen, self.rect.top - margen),
    (self.rect.right + margen, self.rect.top - margen),
    (self.rect.left - margen, self.rect.bottom + margen),
    (self.rect.right + margen, self.rect.bottom + margen),
    (self.rect.centerx, self.rect.centery)
]

            libre = True

            for p in puntos:

                try:
                    color = fondo.get_at(p)

                    # Si toca un arbusto, vuelve a intentar
                    if color.g > 40 and color.g < 120 and color.r < 80:
                        libre = False
                        break

                except:
                    libre = False
                    break

            if libre:
                break