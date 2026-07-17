import pygame
import sys
from assets.src.cabra import Cabra
from assets.src.perro import Perro
from assets.src.manzana import Manzana

pygame.init()

# Ventana
screen = pygame.display.set_mode((1448, 1086))
pygame.display.set_caption("Bambiland")

# Reloj
clock = pygame.time.Clock()

# Fondo
bg = pygame.image.load("assets/images/fondo.png").convert()

# Objetos
cabra = Cabra()
perro = Perro()
manzana = Manzana()

# Primera posición de la manzana
manzana.reubicar(bg)

# Puntos
puntos = 0

# Fuente
fuente = pygame.font.SysFont("Comic Sans MS", 35, True)

# Bucle principal
while True:

    clock.tick(30)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento
    cabra.move(bg)
    perro.follow(cabra, bg)

    # Colisión con la manzana
    if cabra.rect.colliderect(manzana.rect):
        puntos += 1
        manzana.reubicar(bg)

    # Colisión con el perro
    if cabra.rect.colliderect(perro.rect):
        print("GAME OVER")
        pygame.quit()
        sys.exit()

    # Dibujar fondo
    screen.blit(bg, (0, 0))

    # Dibujar objetos
    screen.blit(manzana.sprite, (manzana.x, manzana.y))
    screen.blit(cabra.sprite, (cabra.x, cabra.y))
    screen.blit(perro.sprite, (perro.x, perro.y))

    # Mostrar puntos
    texto = fuente.render("Puntos: " + str(puntos), True, (255, 255, 255))
    screen.blit(texto, (20, 20))

    # Actualizar pantalla
    pygame.display.flip()