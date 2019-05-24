import pygame

# Define constants
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption(f"Title")
clock = pygame.time.Clock()
background = pygame.Surface(gameDisplay.get_size())
background = background.convert()
background.fill(WHITE)

game_quit = False

while not game_quit:

    gameDisplay.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_quit = True
        else:
            print(event)

    pygame.draw.rect(gameDisplay, BLACK, (10, 10, 11, 21))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
