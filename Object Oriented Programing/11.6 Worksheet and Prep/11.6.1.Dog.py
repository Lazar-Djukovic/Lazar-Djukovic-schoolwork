class Dog:
  def __init__(self,myname,mycolour):
    self.name = myname
    self.colour = mycolour
  #endprocedure

  def bark(self, BarkNum):
    for n in range(BarkNum):
      print('Woof')
    #next n
  #endprocedure

  def SetColour(self,DogColour):
	  self.colour = DogColour
  #endprocedure
  
  def GetColour(self): #Why are theese last two defs underlined with red but they work? whats wrong?
	  return(self.colour)

  #endprocedure
  
  def GetName(self):
	  return(self.name)
  #endprocedure
#endclass


