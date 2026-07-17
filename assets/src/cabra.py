import pygame

class Cabra():
    def __init__(self):

        self.sprite = pygame.image.load(
            "assets/images/cabra.png"
        ).convert_alpha()

        self.x = 460
        self.y = 590

        self.rect = self.sprite.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.velocidad = 5

    def move(self, fondo):

        teclas = pygame.key.get_pressed()

        old_x = self.rect.x
        old_y = self.rect.y

        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad

        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad

        if teclas[pygame.K_UP]:
            self.rect.y -= self.velocidad

        if teclas[pygame.K_DOWN]:
            self.rect.y += self.velocidad

        puntos = [
            (self.rect.left, self.rect.top),
            (self.rect.right - 1, self.rect.top),
            (self.rect.left, self.rect.bottom - 1),
            (self.rect.right - 1, self.rect.bottom - 1)
        ]

        for p in puntos:
            try:
                color = fondo.get_at(p)

                if color.g > 40 and color.g < 120 and color.r < 80:
                    self.rect.x = old_x
                    self.rect.y = old_y
                    break

            except:
                self.rect.x = old_x
                self.rect.y = old_y

        self.x = self.rect.x
        self.y = self.rect.y