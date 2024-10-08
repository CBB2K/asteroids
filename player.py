import pygame as pg
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.position = pg.Vector2(x, y)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
    
    def draw(self, screen):
        pg.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        right = pg.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_w]:
            self.move(dt)
        if keys[pg.K_s]:
            self.move(-dt)
        if keys[pg.K_a]:
            self.rotate(-dt)
        if keys[pg.K_d]:
            self.rotate(dt)

    def move(self, dt):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

