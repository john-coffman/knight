import pygame
from Classes.Weapon import Weapon

WIDTH = 1280
HEIGHT = 720


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    weapon1 = Weapon((300, 100))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("white")
        weapon1.update()
        pygame.draw.rect(screen, "black", weapon1)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
