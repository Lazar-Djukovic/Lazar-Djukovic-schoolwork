x = int(input('Please enter a positive integer: '))
if x < 0:
	x = input('Please enter a positive integer: ')
a = x-1
answer = True
done = False

while done == False:
  for count in range(2,a):
    remainder = x % count
    if remainder == 0:
      answer = False
      done = True
  done = True
		
print(answer)
