temp = 0
fever = 0
total = 0
hour = 1
while hour < 7:
	temp = int(input('Enter temperature:'))
	hour = hour + 1
	total = total + temp
	if temp > 37:
		fever = fever + 1
	#endwhile
average = total / hour
print('Average temperature:', average)
print('Incidents of fever:', fever)
