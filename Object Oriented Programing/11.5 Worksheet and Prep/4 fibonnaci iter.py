def fibonacci2(n):
    fibNumbers = [0,1]  #list of first two Fibonacci numbers
	# now append the sum of the two previous numbers to the list    
    for i in (2,n):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
	#next i
    return(fibNumbers[n]) 
#endfunction

myfib = fibonacci2(10)