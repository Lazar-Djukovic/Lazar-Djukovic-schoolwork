temp = 0
fever = 0
total = 0
hour = 1
while (hour < 7)
	temp = int(input('Enter temperature: '))
	if temp > 37 then
		fever = fever + 1
	endif
	total = total + temp
	hour = hour + 1
#endwhile
average = round(total/hour,1) #round to 1 decimal place
print(“Average temperature:”, average)
print(“Incidents of fever:”, fever)
