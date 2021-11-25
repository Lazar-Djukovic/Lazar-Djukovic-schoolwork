total = 0
total_old = 0
partno = ''
while partno != '9999':
    partno = input('Enter Part Number:')
    while len(partno) != 4:
        partno = input('Error: Enter again:')
    #endwhile
    print('correct')
    total = total + 1
    if partno[3] == '6' or partno[3] == '7':
        total_old = total_old + 1
    #endif
#endwhile
print (total, total_old)
