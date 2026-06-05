import pygame

class Perro():

    def __init__(self):

        self.sprite = pygame.image.load(
            "assets/images/perro.gif"
        ).convert_alpha()

        self.x = 850
        self.y = 650

        self.rect = self.sprite.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.velocidad = 2

    def follow(self, cabra):

        if cabra.x > self.x:
            self.x += self.velocidad

        if cabra.x < self.x:
            self.x -= self.velocidad

        if cabra.y > self.y:
            self.y += self.velocidad

        if cabra.y < self.y:
            self.y -= self.velocidad

        self.rect.x = self.x
        self.rect.y = self.y