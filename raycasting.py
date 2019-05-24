from boundary import Boundary
import pygame

# Define constants
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption(f"2D Raycasting")

CLOCK = pygame.time.Clock()

GAME_SURFACE = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

BACKGROUND = pygame.Surface(GAME_SURFACE.get_size())
BACKGROUND = BACKGROUND.convert()
BACKGROUND.fill(BLACK)

GAME_QUIT = False


b = Boundary(300, 300, 300, 100)

while not GAME_QUIT:

    GAME_SURFACE.blit(BACKGROUND, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_QUIT = True
        else:
            # print(event)
            pass

    b.show(GAME_SURFACE)

    pygame.display.update()
    CLOCK.tick(60)

pygame.quit()
quit()
