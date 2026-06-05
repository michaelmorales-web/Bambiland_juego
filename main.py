import pygame
import sys
from assets.src.cabra import Cabra
from assets.src.perro import Perro
from assets.src.manzana import Manzana

pygame.init()

screen = pygame.display.set_mode((1024, 800))
pygame.display.set_caption("Bambiland")

clock = pygame.time.Clock()

bg = pygame.image.load("assets/images/fondo.png").convert()

cabra = Cabra()
perro = Perro()
manzana = Manzana()

puntos = 0

while True:
    clock.tick(30)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    cabra.move(bg)
    perro.follow(cabra)
    if cabra.rect.colliderect(manzana.rect):
            puntos += 1
            manzana.reubicar()
    if cabra.rect.colliderect(perro.rect):
            print("GAME OVER")
            pygame.quit()
            sys.exit()
    screen.blit(bg, (0, 0))
    screen.blit(manzana.sprite, (manzana.x, manzana.y))
    screen.blit(cabra.sprite, (cabra.x, cabra.y))
    screen.blit(perro.sprite, (perro.x, perro.y))
    fuente = pygame.font.SysFont("comic sans ms", 35, True)
    texto = fuente.render(
    "Puntos: " + str(puntos),
    True,
    (255,255,255)
    )
    screen.blit(texto, (20,20))                    
    pygame.display.flip()