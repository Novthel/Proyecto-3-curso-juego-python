import pygame
from constants import HEIGHT_DISPLAY, WIDTH_DISPLAY, COLOR_BG, FPS
from characters import Personaje


jugador = Personaje(50, 50)

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))
pygame.display.set_caption("Primer proyecto animado")

reloj = pygame.time.Clock()


run = True



while run:
    
    reloj.tick(FPS)  # Limit the frame rate to 60 FPS
    
    # Fill the screen with a color (RGB)
    screen.fill(COLOR_BG)  # Blue background
    
    jugador.draw(screen)  # Draw the character on the screen
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jugador.move(-10, 0)  # Move left
            elif event.key == pygame.K_RIGHT:
                jugador.move(10, 0)  # Move right
            elif event.key == pygame.K_UP:
                jugador.move(0, -10)  # Move up
            elif event.key == pygame.K_DOWN:
                jugador.move(0, 10)  # Move down
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jugador.move(0, 0)  # Stop horizontal movement
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                jugador.move(0, 0)  # Stop vertical movement

   
    
    pygame.display.update()  # Update the display

pygame.quit()  # Quit Pygame when the loop ends