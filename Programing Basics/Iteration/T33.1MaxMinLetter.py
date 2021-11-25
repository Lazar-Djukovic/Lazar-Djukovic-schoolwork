maxletter = a
minletter = z
for index = 1 to 5:
    letter = input(“Enter a letter:”)
	if letter > maxLetter then
		maxLetter = letter
	endif
	if letter < minLetter THEN
		minLetter = letter
	endif
next index
print(maxLetter)
print(minLetter)	
