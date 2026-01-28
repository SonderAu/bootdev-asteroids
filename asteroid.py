from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH,ASTEROID_KINDS,ASTEROID_MAX_RADIUS,ASTEROID_MIN_RADIUS,ASTEROID_SPAWN_RATE_SECONDS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        #self.position = pygame.Vector2(x, y)
        super().__init__(x,y,radius)
        #self.radius = radius

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity * dt