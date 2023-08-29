import pygame
from scripts.obj import Obj
from scripts.scene import Scene

class Game(Scene):
    def __init__(self):
        super().__init__()

        self.bg = pygame.image.load("assets/bg.png").convert_alpha()
        self.p1 = pygame.image.load("assets/player1.png").convert_alpha()
        self.p2 = pygame.image.load("assets/player2.png").convert_alpha()
        self.ball = pygame.image.load("assets/ball.png").convert_alpha()

        self.bg_rect = self.bg.get_rect()
        self.p1_rect = self.p1.get_rect()
        self.p2_rect = self.p2.get_rect(right=1280)
        self.ball_rect = self.ball.get_rect(center=[640, 360])

        self.p1_score = 0
        self.p2_score = 0

        self.p1_velocidade = 6

        self.ball_dir_x = 6
        self.ball_dir_y = 6

        self.font = pygame.font.Font(None, 50)

    def events(self, event):
        super().events(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.p1_velocidade = -6
            elif event.key == pygame.K_s:
                self.p1_velocidade = 6

    def draw(self):
        self.display.fill((0, 0, 0))
        self.display.blit(self.bg, self.bg_rect)
        self.display.blit(self.p1, self.p1_rect)
        self.display.blit(self.p2, self.p2_rect)
        self.display.blit(self.ball, self.ball_rect)
        placar_p1 = self.font.render(str(self.p1_score), True, (255, 255, 255))
        placar_p2 = self.font.render(str(self.p1_score), True, (255, 255, 255))
        self.display.blit(placar_p1, (500, 50))
        self.display.blit(placar_p2, (780, 50))

    def update(self):
        self.p1_rect.y += self.p1_velocidade

        if self.p1_rect.top <= 0:
            self.p1_rect.top = 0
        elif self.p1_rect.bottom >= 720:
            self.p1_rect.bottom = 720

        self.ball_rect.x += self.ball_dir_x
        self.ball_rect.y += self.ball_dir_y

        if self.ball_rect.top <= 0 or self.ball_rect.bottom >= 720:
            self.ball_dir_y *= -1

        if self.ball_rect.colliderect(self.p1_rect) or self.ball_rect.colliderect(self.p2_rect):
            self.ball_dir_x *= -1

        if self.ball_rect.left <= 0:
            self.p2_score += 1
            self.reset_ball()

        elif self.ball_rect.right >= 1280:
            self.p1_score += 1
            self.reset_ball()

        if self.p2_rect.centery < self.ball_rect.centery:
            self.p2_rect.y += 6
        elif self.p2_rect.centery > self.ball_rect.centery:
            self.p2_rect.y -= 6

        if self.p1_score >= 3 or self.p2_score >= 3:
            self.active = False

    def reset_ball(self):
        self.ball_rect.center = [640, 360]
        self.ball_dir_x = 6
        self.ball_dir_y = 6

        pygame.time.delay(500)

        self.p1_rect.y = (720 - self.p1_rect.height) / 2
        self.p2_rect.y = (720 - self.p2_rect.height) / 2