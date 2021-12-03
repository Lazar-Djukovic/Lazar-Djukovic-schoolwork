### SRC - Very good.
import pygame
import random
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
# -- Initialise PyGame

pygame.init()
# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("My Window")

# -- Exit game flag set to false
x_direction = 5
y_direction = 5
x_val = 150
y_val = 200
out = False
speed = [5,-5]
counter = 0
life = 5
xpad = 0
ypad = 200
pwid = 15
plen = 60
bwid = 20
done = False
#sysfont = pygame.font.get_default_font()


# -- Manages how fast screen refreshes
clock = pygame.time.Clock() 


### -- Game Loop

while not done:
 # -- User input and controls
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   done = True
#End If
 

 keys = pygame.key.get_pressed() 
  ## - the up key or down key has been pressed 
 if keys[pygame.K_UP]: 
  ypad = ypad - 6
 if keys[pygame.K_DOWN]: 
  ypad = ypad + 6
 if ypad > 420:
     ypad = 420
 if ypad < 0:
     ypad = 0
    
 # - write logic that happens on key press here
 #End If

 rect1 = pygame.Rect(x_val,y_val,bwid,bwid)
 rect2 = pygame.Rect(xpad,ypad,pwid,plen)
 if rect1.colliderect(rect2):
    x_direction = x_direction * -1
 #End If
 #Next event 

 #Next event
 # -- Game logic goes after this comment
 x_val = x_val + x_direction
 y_val = y_val + y_direction

 
 if y_val == 460:
     y_direction = y_direction * -1
 if y_val == 0:
      y_direction = y_direction * -1
 if x_val == 620:
     x_direction = x_direction * -1
 if x_val == 0:
     out = True
     life = life - 1
     x_direction += 5
     y_direction += 5

 if out == True:
  x_direction = 0
  y_direction = 0
  x_val = 300
  y_val = 220
  counter = counter + 1

 if counter >= 30:
     x_direction = random.choice(speed)
     y_direction = random.choice(speed)
     out = False
     counter = 0

 if life == 0:
     done = True
 # -- Screen background is BLACK
 screen.fill (BLACK)

 font2 = pygame.font.SysFont('didot.ttc', 64)
 img2 = font2.render(str(life), True, YELLOW)
 screen.blit(img2, (20, 20))
 # -- Draw here

 pygame.draw.rect(screen, BLUE, (x_val,y_val,bwid,bwid))
 pygame.draw.rect(screen, WHITE, (xpad,ypad,pwid,plen))

 # -- flip display to reveal new position of objects

 pygame.display.flip()

 # - The clock ticks over
 clock.tick(60)

#End While - End of game loop
pygame.quit()
