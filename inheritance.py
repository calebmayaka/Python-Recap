# inheritance is an Object oriented concept in which there is a main class and child classes
# child classes inheriat properties from the main class

class employee:
    def __init__(self,firstname,lastname,dob):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
    def printlastname(self):
        full = self.firstname, self.lastname
        return full
fname = str(input("Enter your firstname: "))
lname = str(input("enter your last name: ")) 
dob = int(input("enter your year of birth: "))
  

employee1 = employee(fname,lname,dob)

print(employee1.firstname)

print(employee1.printlastname())