class Member():

  def __init__(self,mySurname,MyFirstName,myAnnualFee):
		surname = mySurname  
		firstname = MyFirstName
		annualFee = myAnnualFee
	#endprocedure


			#endprocedure
		#Endclass

class JuniorMember(Member):

  def __init__(mySurname,MyFirstName,myAnnualFee,MyDateOfBirth):
    dob = MyDateOfBirth
    super.surname = mySurname  
		super.firstname = MyFirstName
		super.annualFee = myAnnualFee

HarryMason = JuniorMember('Mason','Harry',25,'12.12.2004.')