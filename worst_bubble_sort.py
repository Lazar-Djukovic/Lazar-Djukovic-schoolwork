data = ['B','A','C','F','E','D']

def worst_bubble(arr):

  sorted = False
  while not sorted:
    sorted = True

  for j in range(1,len(arr)):
    for i in range(len(arr)-j):
        if arr[i] > arr[i+1]:
          #swap
          temp = arr[i]
          arr[i] = arr[i+1]
          arr[i+1] = temp
          sorted = False
      #end if
    #next i
  #next j
#end procedure

print(data)
worst_bubble(data)
print(data)