def sum(n):
    if n==0:
        return 0
    if not n % 2 == 0:
        return sum (n-1)
    else:
        return n + sum (n-1)
    #endif
#endprocedure

print(sum(10))
