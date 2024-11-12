import pygame
import math


class Game(object):
    def __init__(self):
        # Настройки окна
            self.WIDTH = 800
            self.HEIGHT = 700
            self.FPS = 120

    def draw_polar_line(self, l1, f1, l2, f2, screen, color):
        center = (self.WIDTH // 2, self.HEIGHT // 2)
        pygame.draw.line(screen, color, 
                        (l1 * math.cos(math.radians(f1)) + center[0], l1 * math.sin(math.radians(f1)) + center[1]), 
                        (l2 * math.cos(math.radians(f2)) + center[0], l2 * math.sin(math.radians(f2)) + center[1]),
                        3
        )

    def draw_polar_dot(self, l, f, screen, color):
        center = (self.WIDTH // 2, self.HEIGHT // 2)
        pygame.draw.circle(screen, color, 
                        (l * math.cos(math.radians(f)) + center[0], l * math.sin(math.radians(f)) + center[1]),
                        3, 5)
        
    def new_start(self, radius):
        points = [(radius, angle / 10) for angle in range(2700, 6300, 5)]
        points_len = len(points)
        return points, points_len

    def main(self, ):
        pygame.init()
        
        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        clock = pygame.time.Clock()
        
        done = False
        
        circle_color = (255, 70, 0)
        triangle_color = (0, 175, 100)

        # Радиус круга
        radius = 300

        # Точки на круге

        points, points_len = self.new_start(radius)
        stage = 0
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    
            screen.fill((214, 204, 203))
            # Отрисовка точек на круге
            for point in points:
                self.draw_polar_dot(point[0], point[1], screen, circle_color)
            
            # Отрисовка треугольника
            match stage:
                case 0:
                    a = points.pop()
                    self.draw_polar_line(points[0][0], points[0][1], a[0], a[1], screen, triangle_color)
                    if len(points) < points_len / 3 * 2:
                        stage = 1
                case 1:
                    self.draw_polar_line(points[0][0], points[0][1], a[0], a[1], screen, triangle_color)
                    b = points.pop()
                    self.draw_polar_line(a[0], a[1], b[0], b[1], screen, triangle_color)
                    if len(points) < points_len / 3:
                        stage = 2
                case 2:
                    self.draw_polar_line(points[0][0], points[0][1], a[0], a[1], screen, triangle_color)
                    self.draw_polar_line(a[0], a[1], b[0], b[1], screen, triangle_color)
                    c = points.pop()
                    self.draw_polar_line(b[0], b[1], c[0], c[1], screen, triangle_color)
                    if len(points) == 1:
                        stage = 3
                case 3:
                    points, points_len = self.new_start(radius)
                    stage = 0
            
            pygame.display.flip()
            clock.tick(self.FPS)
        
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.main()