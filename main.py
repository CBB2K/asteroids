import pygame as pg
from constants import *
from player import Player

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pg.init() 
    
    clock = pg.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        screen.fill("black")
        player.draw(screen)
        pg.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
