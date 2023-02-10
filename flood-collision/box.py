import pygame as pg
from vector import Vector
from random import randint


class Boxes:
    n_boxes = 0
    
    @staticmethod
    def random_posn_velocity(game, max_velocity, width, height):
        left = randint(0, game.window_width - width)
        top = randint(0, game.window_height - height)
        vx = game.speed * randint(1, max_velocity)
        vy = game.speed * randint(1, max_velocity)
        vxsign = randint(0, 1)
        vysign = randint(0, 1)
        vx *= (1 if vxsign == 0 else -1)
        vy *= (1 if vysign == 0 else -1)
        return pg.Rect(left, top, width, height), Vector(vx, vy)
        
    def __init__(self, game, initial_boxes, max_velocity, width, height, color=None, random_sizes=True):
        self.boxes = []
        self.game = game
        for i in range(initial_boxes):
            if random_sizes:
                w = randint(5, game.window_width / 5.0)
                h = randint(5, game.window_height / 5.0)
            else:
                w, h = width, height

            rect, v = Boxes.random_posn_velocity(game, max_velocity, width, height)                
            if color is None:
                color = (randint(0, 255), randint(0, 255), randint(0, 255))
            if color[0] == color[1] == color[2] == 0:
                color[0] += 50

            self.boxes.append(Box(color=color, v=v, rect=rect, game=game))
            Boxes.n_boxes += 1
            
    def add_box(self, color, rect, max_velocity, game):   # TODO add box to self.boxes  AND   increment Boxes.n_boxes
            _, v = Boxes.random_posn_velocity(game, max_velocity, rect.width, rect.height)     
            self.boxes.append(Box(color=color, v=v, rect=rect, game=game))

    def add_random_box(self, color, width, height, max_velocity, game):   # TODO add box to self.boxes  AND   increment Boxes.n_boxes
            rect, v = Boxes.random_posn_velocity(game, max_velocity, width, height)     
            self.boxes.append(Box(color=color, v=v, rect=rect, game=game))

    def update(self):
        for el in self.boxes:
            el.update()
        for el in self.boxes:
            if self.game.player.rect.colliderect(el):
                self.boxes.remove(el)

    def draw(self):
        for el in self.boxes:
            el.draw()


class Box:
    def __init__(self, color, rect, v, game):
        self.screen = game.screen
        self.color = color
        self.rect = rect
        self.v = v
        self.game = game

    def __str__(self):
        return f'Box(clr={self.color},r={self.rect},v={self.v})'

    def update(self):
        self.rect.left += self.v.x
        self.rect.top += self.v.y

        if self.rect.top < 0 or self.rect.bottom > self.game.window_height:
            self.v.y *= -1
        if self.rect.left < 0 or self.rect.right > self.game.window_width:
            self.v.x *= -1
        self.draw()

    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect)
