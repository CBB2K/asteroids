import pygame as pg
from constants import *
from player import Player

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pg.init() 
    
    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    
    #Player.containers = (updatable, drawable)
    
    clock = pg.time.Clock()
    dt = 0
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)

    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        screen.fill("black")

        for obj in updatable:
            obj.update(dt)
        
        for obj in drawable:
            obj.draw(screen)
        
        pg.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
