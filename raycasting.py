from boundary import Boundary
from ray import Ray
import pygame

# Define constants
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

pygame.init()
pygame.display.set_caption(f"2D Raycasting")

CLOCK = pygame.time.Clock()

GAME_SURFACE = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

BACKGROUND = pygame.Surface(GAME_SURFACE.get_size())
BACKGROUND = BACKGROUND.convert()
BACKGROUND.fill(BLACK)

GAME_QUIT = False


wall = Boundary(300, 300, 300, 100)
ray = Ray(100, 200, 0)

ang = 0

while not GAME_QUIT:

    GAME_SURFACE.blit(BACKGROUND, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_QUIT = True
        else:
            # print(event)
            pass

    wall.show(GAME_SURFACE)

    ray.look_at_angle(ang)
    ray.position_at(pygame.mouse.get_pos())
    ang = ang + 1
    if ang == 360:
        ang = 0
    ray.show(GAME_SURFACE)

    point = ray.cast(wall)
    if point:
        pass
        pygame.draw.circle(GAME_SURFACE, GREEN, point, 5)

    pygame.display.update()
    CLOCK.tick(60)

pygame.quit()
quit()
