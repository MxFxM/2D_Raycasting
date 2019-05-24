import pygame


WHITE = (255, 2555, 255)


class Boundary:

    def __init__(self, x1, y1, x2, y2):
        self.a_pos = (x1, y1)
        self.b_pos = (x2, y2)

    def show(self, surface):
        pygame.draw.line(surface, BLACK, a_pos, b_pos)


if __name__ == '__main__':
    print("Please run raycasting.py as main.")
