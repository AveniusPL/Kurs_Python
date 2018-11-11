import pygame
from pygame.math import Vector2


class Rocket(object):

    def __init__(self, game):
        self.game = game
        self.speed = 1.3
        self.gravity = 0.5

        size = self.game.screen.get_size()
        self.pos = Vector2(size[0]/2, size[1]/2)
        self.vel = Vector2(0, 0)  # prędkość
        self.acc = Vector2(0, 0)  # przyspieszenie

    def add_force(self, force):
        self.acc += force

    def tick(self):

        # Input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.add_force(Vector2(0, -self.speed))
        if pressed[pygame.K_s]:
            self.add_force(Vector2(0, self.speed))
        if pressed[pygame.K_a]:
            self.add_force(Vector2(-self.speed, 0))
        if pressed[pygame.K_d]:
            self.add_force(Vector2(self.speed, 0))

        # Physics
        self.vel *= 0.8  # Opór powietrza
        self.vel -= Vector2(0, -self.gravity)

        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def draw(self):

        rect = pygame.Rect(self.pos.x, self.pos.y, 20, 50)
        pygame.draw.rect(self.game.screen, (0, 150, 255), rect)