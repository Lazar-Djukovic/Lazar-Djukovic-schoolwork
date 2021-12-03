import pygame 
import random

# -- Global Constants 

## -- Define the class tile which is a sprite 
class tile(pygame.sprite.Sprite): 
 # Define the constructor for invader 
 def __init__(self, color, width, height, x_ref, y_ref): 
 # Call the sprite constructor 
  super().__init__() 
 # Create a sprite and fill it with colour 
  self.image = pygame.Surface([width,height]) 
  self.image.fill(color) 
  self.rect = self.image.get_rect() 
  # Set the position of the player attributes
  self.rect.x = x_ref 
  self.rect.y = y_ref

def update(self):
  pass

## -- Define the class snow which is a sprite 
class Invader(pygame.sprite.Sprite): 
 # Define the constructor for snow 
 def __init__(self, color, width, height, xpos, ypos, speed): 
 # Call the sprite constructor 
  super().__init__() 
 # Create a sprite and fill it with colour 
  self.ypos = ypos
  self.xpos = xpos
  self.speed = speed
  self.image = pygame.Surface([width,height]) 
  self.image.fill(color) 
 # Set the position of the sprite 
  self.rect = self.image.get_rect() 
  self.rect.x = self.xpos
  self.rect.y = self.ypos

 def update(self):
   pass


class Player(pygame.sprite.Sprite):
   #the constructor
   def __init__(self, color, width, height):
      # Call the sprite constructor 
      super().__init__() 
      self.speedx = 0
      self.speedy = 0
   # Create a sprite and fill it with colour 
      self.image = pygame.Surface([width,height]) 
      self.image.fill(color) 
      # Set the position of the sprite 
      self.rect = self.image.get_rect() 
      self.rect.x = 20
      self.rect.y = 20

   def update(self):
      self.rect.x = self.rect.x + self.speedx
      self.rect.y = self.rect.y + self.speedy

   def player_set_speed(self, speedx, speedy):
       self.speedx = speedx
       self.speedy = speedy


 #End Procedure
#End Class

map = [[1,1,1,1,1,1,1,1,1,1], 
      [1,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,1], 
      [1,1,0,1,1,1,1,1,0,1], 
      [1,0,0,0,0,0,1,0,0,1],
      [1,0,1,1,1,0,1,0,0,1],
      [1,0,1,1,1,0,1,0,0,1], 
      [1,0,1,1,1,0,1,0,0,1], 
      [1,0,0,0,0,0,0,0,0,1], 
      [1,1,1,1,1,1,1,1,1,1]]


# -- Colours 
BLACK = (0,0,0) 
WHITE = (255,255,255) 
BLUE = (50,50,255) 
YELLOW = (255,255,0) 
RED = (255, 50, 50)

# -- Initialise PyGame
pygame.init() 

# -- Blank Screen 
size = (640,480) 
screen = pygame.display.set_mode(size) 

# -- Title of new window/screen 
pygame.display.set_caption("My Window") 

# -- Exit game flag set to false 
done = False

# Create a list of all sprites 
all_sprites_list = pygame.sprite.Group() 
 

# Create a list of the snow blocks 
invader_group = pygame.sprite.Group()
# Create a list of all sprites 
all_sprites_group = pygame.sprite.Group() 

#Next x
theplayer = Player(RED, 10, 10)
all_sprites_group.add (theplayer)

# -- Manages how fast screen refreshes 
clock = pygame.time.Clock() 

# Create a list of tiles for the walls 
wall_list = pygame.sprite.Group()
 
# Create walls on the screen (each tile is 20 x 20 so alter cords)
for row in range(10):
  for col in range (10):
    if map[row][col] == 1: 
      my_wall = tile(BLUE, 20, 20,col*20, row*20) 
      wall_list.add(my_wall) 
      all_sprites_group.add(my_wall)


### -- Game Loop 
while not done: 
 # -- User input and controls 
 for event in pygame.event.get(): 
   if event.type == pygame.QUIT: 
         done = True 
#End If
 #Next event

#movement
# -- User inputs here 
   elif event.type == pygame.KEYDOWN: # - a key is down 
      if event.key == pygame.K_LEFT: # - if the left key pressed
       theplayer.player_set_speed(-3, 0) # speed set to -3
      elif event.key == pygame.K_RIGHT: # - if the right key pressed
       theplayer.player_set_speed(3, 0) # speed set to 3
      elif event.key == pygame.K_UP: # - if the left key pressed
       theplayer.player_set_speed(0,-3) # speed set to -3
      elif event.key == pygame.K_DOWN: # - if the right key pressed
       theplayer.player_set_speed(0,3) # speed set to 3
      #endif
   elif event.type == pygame.KEYUP: # - a key released 
     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
      theplayer.player_set_speed(0, 0) # speed set to 0
     elif event.key == pygame.K_UP or event.key == pygame.K_DOWN: 
      theplayer.player_set_speed(0, 0) # speed set to 0
   #endif
 # -- Game logic goes after this comment

 # -- Check for collisions between pacman and wall tiles 
 player_hit_list = pygame.sprite.spritecollide(theplayer, wall_list, False)
 print (theplayer.rect.x) 
 for foo in player_hit_list: 
   theplayer.set_speed(0, 0) 
 
 # Run the update function for all sprites 
 all_sprites_list.update()

 #endif


 #-update all sprites
 all_sprites_group.update() 

 # -- Screen background is BLACK 
 screen.fill (BLACK) 

 # -- Draw here 
 all_sprites_group.draw(screen)

 # -- flip display to reveal new position of objects 
 pygame.display.flip()
 # - The clock ticks over 
 clock.tick(60) 

#End While - End of game loop 
pygame.quit()

