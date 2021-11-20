import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

 

class Snow:
    def __init__(self):
        self.colour = WHITE
        self.height = 10
        self.width = 10
        self.listx = []
        self.listy = []
        for i in range(0,110):
             x = random.randrange(0, 700)
             y = random.randrange(-70, 400)
             self.listx.append(x)
             self.listy.append(y)

    #end procedure 
#end class
        

    def update(self):

        for i in range(len(self.listx)):
            pygame.draw.rect(screen, self.colour, (self.listx[i],self.listy[i],self.height,self.width))
            self.listy[i] += 1
            if self.listy[i] > 500:
                self.listy[i] = -10
                x = random.randrange(0, 700)
                self.listx[i] = x


        

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
snow1 = Snow()

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    
    snow1.update()
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()