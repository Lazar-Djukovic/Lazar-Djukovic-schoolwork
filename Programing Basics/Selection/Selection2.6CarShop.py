cars = ['Economy Car','Saloon Car','Sports Car']
max = len(cars)
print ('[ Available cars are: ]')

index = 0
while index < len(cars):
  print (index,cars[index])
  index = index + 1
found = False
counter = 0 
choice = int(input('[Select a car]'))

while counter < max and found == False:
  if choice > -1 and choice < len(cars):
    counter = counter + 1
    print('valid choice')
    found = True
    c2 = input('Do you wish to proceed?  Y/N  ')
    if c2 == 'y':
      print ('Response confirmed')
      print ('Have a nice day')
    else: print('Alright have a nice day')
  else: counter = counter + 1
  #endif

#endwhile

if found == False:
  print('Invalid')
 #end if