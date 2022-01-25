#rock paper scissors game

import random

r = ['null','rock','paper','scissors']
c = ['1','2','3']

turn = False
game = True
check = False


print('================================================')
print(' Welcome to rock paper scissors, please select:')
print('1. Rock')
print('2. Paper')
print('3. Scissors')
print('================================================')

while turn == False:

  while check == False:
    playerc = input('Please make your selection =>')
    if playerc in c:
      print('Valid choice')
      check = True
    else:
      print('Invalid choice')

  computer = r[random.randint(1,3)]

  player = r[int(playerc)]


  while game == True:
    if player == computer:
      print('computer choice was: '+ computer)
      print('your choice was: '+ player)
      print('Draw!')
      game = False
    
    elif player == r[1] and computer == r[2]:
      print('computer choice was: '+ str(computer))
      print('your choice was: '+ player)
      print('Computer wins!')
      game = False
    
    elif player == r[1] and computer == r[3]:
      print('computer choice was: '+ str(computer))
      print('your choice was: '+ player)
      print('You Win!')
      game = False
    
    elif player == r[2] and computer == r[1]:
      print('computer choice was: '+ str(computer))
      print('your choice was: '+ player)
      print('You Win!')
      game = False
    
    elif player == r[2] and computer == r[3]:
      print('computer choice was: '+ str(computer))
      print('your choice was: '+ player)
      print('Computer wins!')
      game = False
    
    elif player == r[3] and computer == r[1]:
      print('computer choice was: '+ str(computer))
      print('your choice was: '+ player)
      print('Computer wins!')
      game = False

    elif player == r[3] and computer == r[2]:
      print('computer choice was: '+ str(computer))
      print('your choice was: '+ player)
      print('You win!')
      game = False
    #endif
  #endwhile

  game = True
  check = False
