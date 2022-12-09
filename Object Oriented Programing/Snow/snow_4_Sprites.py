### SRC - Really good, but try using some layers
import pygame
import random
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
## -- Define the class house which is a sprite 
class House(pygame.sprite.Sprite): 
# Define the constructor for house 
  def __init__(self, color, width, height, posx, posy): 
  # Call the sprite constructor 
    super().__init__() 
    # Create a sprite and fill it with colour 
    self.image = pygame.Surface([width,height]) 
    self.image.fill(color) 
    # Set the position of the sprite 
    self.rect = self.image.get_rect() 
    self.rect.x = posx
    self.rect.y = posy
  #End Procedure
  
  def update(self):
    pass
#End Class

## -- Define the class snow which is a sprite 
class Snow(pygame.sprite.Sprite): 
# Define the constructor for snow 
  def __init__(self, color, width, height, speed): 
  # Call the sprite constructor 
    super().__init__() 
    # Create a sprite and fill it with colour 
    self.image = pygame.Surface([width,height]) 
    self.image.fill(color) 
    # Set speed of the sprite 
    self.speed = speed 
    # Set the position of the sprite 
    self.rect = self.image.get_rect() 
    self.rect.x = random.randrange(0, 700) 
    self.rect.y = random.randrange(0, 500) 
  #End Procedure
  
  def update(self):
    self.rect.y = self.rect.y + self.speed 
    if self.rect.y > 500:
      self.rect.y = -10
#End Class


pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False

# Create a list of the snow blocks 
snow_group = pygame.sprite.Group() 

# Create a list of all sprites 
all_sprites_group = pygame.sprite.Group() 

#add the house to the group of sprites
redhouse = House(RED, 100, 50, 50, 450)
greenhouse = House(GREEN, 100, 50, 400, 450)
all_sprites_group.add(redhouse)
all_sprites_group.add(greenhouse)
# Create the snowflakes 
number_of_flakes = 50 # we are creating 50 snowflakes
for x in range (number_of_flakes): 
  my_snow = Snow(WHITE, 5, 5, 1) # snowflakes are white with size 5 by 5 px
  snow_group.add (my_snow) # adds the new snowflake to the group of snowflakes
  all_sprites_group.add (my_snow) # adds it to the group of all Sprites
#Next x

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    all_sprites_group.update()
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here

    all_sprites_group.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
