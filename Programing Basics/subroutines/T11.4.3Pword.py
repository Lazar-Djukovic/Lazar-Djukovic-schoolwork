#Write pseudocode for a subroutine called getPword() that takes one parameter, called attempt, which can have a value of 1 or 2. 
#The subroutine should prompt the user to enter a password if attempt = 1, or prompt the user to re-enter a password if the attempt = 2,
#and then return the password.  
#The subroutine should also check that the length of the password is a valid length between 6 to 8 characters. 
#The main program will verify that the two passwords are the same, and re-prompt for entry if they are not.
# If both passwords are the same, a message is displayed, informing the user that the password change has been successful. 

def getpword(attempt):
    if len(attempt) > 6 and len(attempt) < 8:
        print('Enter password again')
        pword2 = input(' ')
        if pword2 == attempt:
            print('password change successful')
            return(1)
        else:
            print('Error, passwords do not match')
        #endif
    else:
        print('Error, password must be 6 to 8 characters long')

    #endif

#main code starts here
done = False
while done == False:
 print('Enter password:')
 pword = input(' ')
 doneif = getpword(pword)
 if doneif == 1:
     done = True
#endwhile