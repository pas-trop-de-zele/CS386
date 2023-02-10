import pygame as pg
from vector import Vector
from colors import RED, GREEN, BLUE, PURPLE, CYAN


class Circles:
    def __init__(self, game):
        self.circles = []
        self.circles.append(Circle(screen=game.screen, color=RED, v=game.speed * Vector(1.0, -2.0),
                                   center=Vector(100, 100), radius=30, game=game))
        self.circles.append(Circle(screen=game.screen, color=GREEN, v=game.speed * Vector(-1.0, -1.0),
                                   center=Vector(200, 200), radius=20, game=game))
        self.circles.append(Circle(screen=game.screen, color=BLUE, v=game.speed * Vector(1.0, 1.0),
                                   center=Vector(100, 150), radius=50, game=game))
        self.circles.append(Circle(screen=game.screen, color=PURPLE, v=game.speed * Vector(1.0, 2.0),
                                   center=Vector(300, 200), radius=60, game=game))
        self.circles.append(Circle(screen=game.screen, color=CYAN, v=game.speed * Vector(1.0, -3.0),
                                   center=Vector(150, 50), radius=40, game=game))

    def update(self):
        for el in self.circles:
            el.update()

    def draw(self):
        for el in self.circles:
            el.draw()


class Circle:
    def __init__(self, screen, color, center, radius, v, game):
        self.screen = screen
        self.color = color
        self.center = center
        self.radius = radius
        self.v = v
        self.game = game

    def __str__(self):
        return f'Circle(clr={self.color},ctr={self.center},r={self.radius},v={self.v})'

    def update(self):
        self.center += self.v
        # self.center.x += self.v.x
        # self.center.y += self.v.y

        if self.center.y < self.radius or self.center.y > self.game.window_height - self.radius:
            self.v.y *= -1
        if self.center.x < self.radius or self.center.x > self.game.window_width - self.radius:
            self.v.x *= -1
        self.draw()

    def draw(self):
        c = self.center
        pg.draw.circle(self.screen, self.color, (c.x, c.y), self.radius)
