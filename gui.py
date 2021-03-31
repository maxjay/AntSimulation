import pygame
from ant import Ant


ants = [Ant() for i in range(50)]
camera = [250, 250]

pygame.init()
screen = pygame.display.set_mode([500, 500])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("hello") 
                camera[0] -= 1
    screen.fill((255, 255, 255))
    for i in ants:
        pygame.draw.circle(screen, (0, 0, 255), (i.x + camera[0], i.y + camera[1]), 1)
        i.update()
    pygame.display.flip()
    

pygame.quit()