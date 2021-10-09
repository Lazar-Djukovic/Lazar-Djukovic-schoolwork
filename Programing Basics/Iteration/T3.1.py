x = int(input('enter first'))
y = int(input('enter second'))
z = 0
while x > 0:
    if x / 2 == 1:
     z = z + y
    #endif
x = x / 2
y = y * 2
#endwhile
print ("Answer =", z)	
