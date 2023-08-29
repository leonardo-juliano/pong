import pygame
from scripts.scene import Scene

class Menu(Scene):
    def __init__(self):
        super().__init__()
        self.menu_img = pygame.image.load("assets/menu.png")
        self.menu_rect = self.menu_img.get_rect()

    def events(self, event):
        super().events(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False
                start = pygame.mixer.Sound("assets/start.wav")
                start.play()

    def draw(self):
        self.display.fill((0, 0, 0))
        self.display.blit(self.menu_img, self.menu_rect)

    def update(self):
        pass
