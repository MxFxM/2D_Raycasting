import math

WHITE = (255, 255, 255)


class Ray:

    def __init__(self, x1, y1, a):
        self.position = (x1, y1)
        x_part = math.cos(2 * pi * a / 360)
        y_part = math.sin(2 * pi * a / 360)
        self.direction = (x_part, y_part)

    def show(self, surface):
        pygame.draw.line(surface, WHITE, self.position, (round((p+d)*10)
                                                         for p, d in zip(self.position, self.direction)))
