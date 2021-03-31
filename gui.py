import pygame
from ant import Ant

pygame.init()
class Simulation():
    def __init__(self, width=1280, height=720):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode([width, height])
        self.running = True
        self.ants = [Ant() for i in range(50)]
        self.camera = [width/2, height/2]

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_w]:
                self.camera[1] += 1
            if keys_pressed[pygame.K_s]:
                self.camera[1] -= 1
            if keys_pressed[pygame.K_a]:
                self.camera[0] += 1
            if keys_pressed[pygame.K_d]:
                self.camera[0] -= 1
            self.screen.fill((255, 255, 255))
            for i in self.ants:
                pygame.draw.circle(self.screen, (0, 0, 255), (i.x + self.camera[0], i.y + self.camera[1]), 1)
                if (i.y > self.height/2 or i.y < -self.height/2):
                    i.bumpY()
                if (i.x > self.width/2 or i.x < -self.width/2):
                    i.bumpX()
                i.update()
            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    a = Simulation()
    a.run()