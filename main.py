import sys

import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from logger import log_event, log_state
from player import Player


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for drawable_item in drawable:
            drawable_item.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")


if __name__ == "__main__":
    main()

