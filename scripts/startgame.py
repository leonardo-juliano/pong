import pygame
from scripts.menu import Menu
from scripts.game import Game

class StartGame:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.display = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("StartGame")

        self.clock = pygame.time.Clock()
        self.scenes = [Menu(), Game()]
        self.active_scene = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.active = False
            else:
                self.scenes[self.active_scene].events(event)

    def update(self):
        self.scenes[self.active_scene].update()
        if not self.scenes[self.active_scene].active:
            self.active_scene = (self.active_scene + 1) % len(self.scenes)
            self.scenes[self.active_scene].active = True

    def render(self):
        self.scenes[self.active_scene].draw()
        pygame.display.flip()

    def run(self):
        self.active = True
        while self.active:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

        pygame.quit()

