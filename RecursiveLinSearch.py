array = (2,3,5,7,11,13,17,19,23)

a = int(input('search the array for a number '))
b = 0

def Rec_LinSearch(a,b):

  if a == array[b]:
    return(b)
  
  else:
    Rec_LinSearch(a,b+1)


print(Rec_LinSearch(a,b))