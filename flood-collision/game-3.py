import pygame as pg, sys, time
from box import Boxes, Box
from circle import Circles
from colors import DARK_GREY, GREEN, RED
from vector import Vector
from random import randint


class Game:
    def __init__(self): 
        pg.init()
        self.window_height = 400
        self.window_width = 400
        self.screen = pg.display.set_mode((self.window_width, self.window_height), 0, 32)
        pg.display.set_caption('Animation')
        self.speed = 6
        self.player = Box(color=RED, rect=pg.Rect(300, 100, 50, 50), v=Vector(), game=self)
        self.boxes = Boxes(game=self, initial_boxes=40, max_velocity=2, width=20, height=20,
                           color=GREEN, random_sizes=False)
        # self.circles = Circles(game=self)

    def play(self):
        keys = [pg.K_w, pg.K_s, pg.K_a, pg.K_d]
        keys_dir = {pg.K_w: Vector(0, -1), pg.K_s: Vector(0, 1), pg.K_a: Vector(-1, 0),
                    pg.K_d: Vector(1, 0)}
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    key = event.key
                    if key in keys:
                        self.player.v += self.speed * keys_dir[key]
                    elif key == pg.K_x:
                        r = self.player.rect
                        self.player.rect.top = randint(0, self.window_height - r.height)
                        self.player.rect.left = randint(0, self.window_width - r.width)
                elif event.type == pg.KEYUP:
                    key = event.key
                    if key in keys:
                        self.player.v = Vector()
                elif event.type == pg.MOUSEBUTTONUP:
                    self.boxes.add_box(color=GREEN, rect=pg.Rect(event.pos[0], event.pos[1], 20, 20),
                                       max_velocity=3, game=self)
                if Boxes.n_boxes > 40: pass
                    
            self.screen.fill(DARK_GREY)
            self.boxes.update()
            self.player.update()
            # self.circles.update()
            pg.display.update()
            time.sleep(0.02)


def main():
    g = Game()
    g.play()
    
    
if __name__ == '__main__':
    main()

 