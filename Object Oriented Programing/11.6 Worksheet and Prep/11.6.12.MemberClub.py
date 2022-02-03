class Member():

  def __init__(self,mySurname,MyFirstName,myAnnualFee):
    self.surname = mySurname  
    self.firstname = MyFirstName
    self.annualFee = myAnnualFee
	#endprocedure


			#endprocedure
		#Endclass

class JuniorMember(Member):

  def __init__(mySurname,MyFirstName,myAnnualFee,MyDateOfBirth):
    super.dob = MyDateOfBirth
    super.surname = mySurname  
    super.firstname = MyFirstName
    super.annualFee = myAnnualFee

HarryMason = JuniorMember('Mason','Harry',25,'12.12.2004.')