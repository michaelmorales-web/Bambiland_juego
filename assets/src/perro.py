import pygame


class Perro:

    def __init__(self):

        self.sprite = pygame.image.load(
            "assets/images/perro.png"
        ).convert_alpha()

        self.rect = self.sprite.get_rect()

        self.rect.x = 900
        self.rect.y = 720

        self.x = self.rect.x
        self.y = self.rect.y

        self.velocidad = 2

    def puede_mover(self, fondo, x, y):

        puntos = [
            (x, y),
            (x + self.rect.width - 1, y),
            (x, y + self.rect.height - 1),
            (x + self.rect.width - 1, y + self.rect.height - 1)
        ]

        for p in puntos:

            try:
                color = fondo.get_at(p)

                if color.g > 40 and color.g < 120 and color.r < 80:
                    return False

            except:
                return False

        return True

    def follow(self, cabra, fondo):

        movimientos = []

        dx = cabra.rect.x - self.rect.x
        dy = cabra.rect.y - self.rect.y

        # Prioriza el eje donde la distancia es mayor
        if abs(dx) > abs(dy):

            if dx > 0:
                movimientos.append((self.velocidad, 0))
            else:
                movimientos.append((-self.velocidad, 0))

            if dy > 0:
                movimientos.append((0, self.velocidad))
            else:
                movimientos.append((0, -self.velocidad))

        else:

            if dy > 0:
                movimientos.append((0, self.velocidad))
            else:
                movimientos.append((0, -self.velocidad))

            if dx > 0:
                movimientos.append((self.velocidad, 0))
            else:
                movimientos.append((-self.velocidad, 0))

        # Agrega movimientos alternativos para rodear paredes
        movimientos.extend([
            (self.velocidad, 0),
            (-self.velocidad, 0),
            (0, self.velocidad),
            (0, -self.velocidad)
        ])

        for mx, my in movimientos:

            nx = self.rect.x + mx
            ny = self.rect.y + my

            if self.puede_mover(fondo, nx, ny):
                self.rect.x = nx
                self.rect.y = ny
                break

        self.x = self.rect.x
        self.y = self.rect.y