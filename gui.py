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
        self.zoom = 1

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEWHEEL:
                    if pygame.key.get_mods():
                        if event.y < 0:
                            self.zoom = max(1, self.zoom-1)
                        else:
                            self.zoom += 0.1
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
                pygame.draw.circle(self.screen, (0, 0, 255), (i.x*self.zoom + self.camera[0], i.y*self.zoom + self.camera[1]), self.zoom*1.25)
                if (i.y > self.height/2*self.zoom or i.y < -self.height/2*self.zoom):
                    i.bumpY()
                if (i.x > self.width/2*self.zoom or i.x < -self.width/2*self.zoom):
                    i.bumpX()
                i.update()
            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    a = Simulation()
    a.run()