import pygame
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
BLUE = (100,100,255)
YELLOW = (255,255,0)
BROWN = (210,105,30)
GREEN = (80,255,40)
RED = (175,13,8)
BRICK = (245,85,57)
GRAY = (161, 165, 162)
LBLUE = (135,206,235)
DBLUE = (0,33,66)
# -- Initialise PyGame

pygame.init()
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen

pygame.display.set_caption("My Window")
# -- Exit game flag set to false
day = True
rise = True
cyp = 100
yy = 465
done = False
counter = 0
# -- Manages how fast screen refreshes

clock = pygame.time.Clock() 
cxp = 40
### -- Game Loop

while not done:
 # -- User input and controls
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   done = True
#End If
 #Next event
 # -- Game logic goes after this comment

 if day == True:
    cxp = cxp + 1

 if cyp < 70 and day == True:
    rise = False
 else:
    cyp = cyp - 0.1
    cxp = cxp - 0.1
   
 if rise == False:
    cyp = cyp + 0.2
    cxp = cxp + 0.1
 else: 
    rise = True

 if day == False:
    screen.fill (DBLUE)
 else:
    screen.fill (LBLUE)

 if cxp > 680:
     day = False
     counter = counter + 1
 else:
  cxp = cxp

 if counter == 100:
    day = True
    cxp = 40
    cyp = 100
    rise = True
    counter = 0
    


 


 # -- Draw here

 pygame.draw.rect(screen, BRICK, (220,165,200,150))
 pygame.draw.circle(screen, YELLOW, (cxp,cyp),40,0)
 for yy in range (165,320,13):
    pygame.draw.line(screen, GRAY, (220,yy),(420,yy),2)
 for xx in range (220,420,33):
    pygame.draw.line(screen, GRAY, (xx,165),(xx,320),2)
 pygame.draw.rect(screen, BROWN, (300,250,40,65))
 pygame.draw.rect(screen, BLUE, (240,190,30,25))
 pygame.draw.rect(screen, BLUE, (240,240,30,25))
 pygame.draw.rect(screen, BLUE, (370,190,30,25))
 pygame.draw.rect(screen, BLUE, (370,240,30,25))
 pygame.draw.polygon(screen, RED, ((220,166),(320,130),(420,166)))
 pygame.draw.rect(screen, GREEN, (0,315,640,170))
 
 # -- flip display to reveal new position of objects
 pygame.display.flip()

 # - The clock ticks over
 clock.tick(60)

#End While - End of game loop

pygame.quit()