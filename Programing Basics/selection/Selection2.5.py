MovementGround = True
MovementFirst = True
TriggerON = True
if TriggerON == True: 
    if MovementGround == True and MovementFirst == False:
        print('Intruder on ground floor')
    elif MovementGround == False and MovementFirst == True:
        print('Intruder on first floor')
    elif MovementGround == True and MovementFirst == True:
        print('Intruder on ground floor')
        print('Intruder on first floor')
    else:
         print('No movement detected')
    #endif
 #endif
