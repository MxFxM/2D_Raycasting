from ray import Ray
import pygame


GREEN = (0, 255, 0)


class Particle:

    def __init__(self, x, y, beams):
        self.position = (x, y)
        self.rays = []
        for i in range(beams):
            self.rays.append(Ray(x, y, 360 * i / beams))

    def position_at(self, pos):
        for ray in self.rays:
            ray.position_at(pos)

    def show(self, gs):
        for ray in self.rays:
            ray.show(gs)

    def cast(self, gs, wall):
        for ray in self.rays:
            point = ray.cast(wall)
            if point:
                pygame.draw.circle(gs, GREEN, point, 5)


if __name__ == '__main__':
    print("Please run raycasting.py as main.")
