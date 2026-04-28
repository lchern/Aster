import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60)/1000

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")



if __name__ == "__main__":
    main()
