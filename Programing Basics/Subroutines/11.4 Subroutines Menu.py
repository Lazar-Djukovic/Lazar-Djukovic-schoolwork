def displaymenu():
  print('=================')
  print('1. Add name')
  print('2. Display list')
  print('3. Quit')
  print('=================')
  Choices = [0,1,2]
  Choice = int(input('Select 1-3: '))
  while Choice < 1 or Choice > 3:
    print('Invalid choice')
    Choice = int(input('Please re-enter choice: '))
    print(' ')
  print('thanks')

choice = displaymenu()
