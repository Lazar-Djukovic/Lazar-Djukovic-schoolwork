class Dog():
  #name as string
  #colour as string
  def __init__(self, myName, myColour):
    self.name = myName #Private
    self.colour = myColour
    #end if
  #end procedure
  
  def get_colour(self): #Public
    return self.colour
  #end function
  def set_colour(self,myColour): #Public
    if myColour == 'unknown':
      self.colour = input('Enter a colour')
    else:
      self.colour = myColour
    #end if
  #end procedure
  def bark(barkTimes):
    for n in range(barkTimes):
      print ("Woof!")
    #next n
  #end procedure
#end class
class Puppy(Dog):
  #private shoesChewed = 0
  def __init__ (self,myName, myColour, myDob):
    super().__init__(myName, myColour)
    self.dob = myDob
    self.shoesChewed = 0
  #end procedure
#end class
#main
myFirstPuppy = Puppy('Sam','Grey','01/01/2021')
print(myFirstPuppy.dob)
myFirstDog = Dog('Fido','Brown')
myFirstDog.set_colour('Pink')
print(myFirstDog.get_colour())
myDog3 = Dog('Mutton','unknown')
print(myDog3.get_colour())
myDog3.set_colour('unknown')
print(myDog3.get_colour())
