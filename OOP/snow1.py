import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

fs = 10
 
snowx1 = 0
snowy1 = 0


class Snow:
    def __init__(self):
        self.x = 100
        self.y = 0
        self.colour = WHITE
        self.height = 10
        self.width = 10
        
    #end procedure 
#end class
    def draw(self):
        pygame.draw.rect(screen,self.colour, [self.x,self.y,self.height,self.width])
    
    def update(self):
        if self.y > 500:
            self.x = random.randint(0,700)
            self.y = 0
        else 
        self.1.y = self.1.y +1

        

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
snow1 = Snow()
print(snow1.x)
print(snow1.y)
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    snow1.y = snow1.y + 3

    if snow1.y > 500:
        snow1.y = 0
        snow1.x = random.randint(0,700)
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    snow1.draw()
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()