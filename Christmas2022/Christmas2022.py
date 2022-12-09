import pygame
import math
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
display = pygame.display.set_mode(size)

font = pygame.font.SysFont("Verdana",25)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Loading images
santa_img = pygame.image.load('santa.png').convert()
santa_main_img = pygame.transform.scale(santa_img,(64,64))
santa_main_img.set_colorkey((BLACK))

gifts = []
gift_speed = 2

gift_1 = pygame.image.load('gift_1.png').convert()
gift_1 = pygame.transform.scale(gift_1,(32,32))
gift_1.set_colorkey((BLACK))
gifts.append(gift_1)

gift_2 = pygame.image.load('gift_2.png').convert()
gift_2 = pygame.transform.scale(gift_2,(32,32))
gift_2.set_colorkey((BLACK))
gifts.append(gift_2)

gift_3 = pygame.image.load('gift_3.png').convert()
gift_3 = pygame.transform.scale(gift_3,(32,32))
gift_3.set_colorkey((BLACK))
gifts.append(gift_3)

background = pygame.image.load('background.png').convert()
#End of loading images

#Classes

class Santa(pygame.sprite.Sprite):
  def __init__(self, x, y, size):
    super().__init__()
    self.size = size
    self.image = pygame.Surface([self.size,self.size])
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.speed = 5

    self.score = 0

    self.change_x = 0
    self.change_y = 0

  def changespeed(self, x):

    self.change_x += x


  def update(self,display):

    display.blit(santa_main_img,(self.rect.x,self.rect.y))

    self.rect.x += self.change_x

    img = font.render('Score: '+ str(self.score), True, GREEN)
    display.blit(img,(0,0))




class Gift(pygame.sprite.Sprite):
  def __init__(self, x, y, size):
    super().__init__()
    self.size = size
    self.image = pygame.Surface([self.size,self.size])
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.speed = gift_speed

    self.type = random.randint(0,2)

  def update(self,display):
    
    display.blit(gifts[self.type],(self.rect.x,self.rect.y))
    self.rect.y += self.speed

    if self.rect.y > 440:
      all_sprites_group.remove(self)



class Snow(pygame.sprite.Sprite):
  def __init__(self, width,height):
    super().__init__()
    self.size = size
    self.image = pygame.Surface([width,height]) 
    self.image.fill(WHITE) 
    self.rect = self.image.get_rect()

    self.rect.x = random.randrange(0, 700) 
    self.rect.y = random.randrange(-50, 50) 

    self.speed = 1

  def update(self,display):
    
    self.rect.y += self.speed

    if self.rect.y > 440:
      all_sprites_group.remove(self)
      snow_group.remove(self)


all_sprites_group = pygame.sprite.Group() 
santa_group = pygame.sprite.Group() 
gift_group = pygame.sprite.Group() 
snow_group = pygame.sprite.Group() 


mysanta = Santa(300,400,64)
all_sprites_group.add(mysanta)
santa_group.add(mysanta)


index = 0
diff = 0


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mysanta.changespeed(-3)
            elif event.key == pygame.K_RIGHT:
                mysanta.changespeed(3)
 
        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                mysanta.changespeed(3)
            elif event.key == pygame.K_RIGHT:
                mysanta.changespeed(-3)


    diff += 1
    index += 1
    if index > 75:
      mygift = Gift(random.randint(0,700),0,32)
      all_sprites_group.add(mygift)
      gift_group.add(mygift)
      index = 0
    
    #gifts fall faster after some time
    if diff > 1000:
      gift_speed += 1
      diff = 0

    display.blit(background,(0,0))

    santa_gift_list = pygame.sprite.groupcollide(santa_group , gift_group, False, True)
    for gift in santa_gift_list:
      mysanta.score += 1


    size = random.randint(2,4)
    my_snow = Snow(size, size) 
    snow_group.add (my_snow) 
    all_sprites_group.add (my_snow) 
 

    # --- Drawing code should go here

    all_sprites_group.update(display)
    snow_group.draw(display)

    pygame.display.flip()
 
    
    clock.tick(60)
    pygame.display.update()


pygame.quit()
