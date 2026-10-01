import pygame

from constants import COLOR_CHARACTER, HEIGHT_CHARACTERS, WIDTH_CHARACTERS

class Personaje():
    def __init__(self, x, y):
        self.shape = pygame.Rect(0, 0, WIDTH_CHARACTERS, HEIGHT_CHARACTERS)
        self.shape.center = (x, y)
       
        
    def draw(self, screen):
        pygame.draw.rect(screen, COLOR_CHARACTER, self.shape)  # Draw a red rectangle representing the character

    def move(self, dx, dy):
        self.shape.x =  self.shape.x + dx
        self.shape.y =  self.shape.y + dy
        
    