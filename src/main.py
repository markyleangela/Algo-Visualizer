import pygame

pygame.init()

if __name__ == '__main__':
    SCREEN_WIDTH, SCREEN_HEIGHT = 1100, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        screen.fill((0, 0, 0))
        pygame.display.update()