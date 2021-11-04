def multiple (start,end,value,pupilname):
    print('Hi ',pupilname,'here is your timestable')
    for x in range (start,end + 1):
        print(x,'x', value, 'is', x * value)
    #next x

name = input('Whats your name?')
print('enter table, start num and end num')
table = int(input())
startnum = int(input())
endnum = int(input())


multiple(startnum,endnum,table,name)
print('next')