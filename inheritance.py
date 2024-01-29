# inheritance is an Object oriented concept in which there is a main class and child classes
# child classes inherit properties from the main class

class employee:
    def __init__(self,firstname,lastname,dob):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
    def printfullname(self):
        full = self.firstname, self.lastname
        return full
fname = str(input("Enter your firstname: "))
lname = str(input("enter your last name: ")) 
dob = int(input("enter your year of birth: "))
  

employee1 = employee(fname,lname,dob)

print(employee1.firstname)

print(employee1.printfullname())

class softwaredev(employee):
    def __init__(self,firstname,lastname,dob,language):
        super().__init__(firstname,lastname,dob)
        self.language  = language

languagein = str(input("Enter Your Programming Language:"))
dev1 = softwaredev(fname,languagein, lname, lname)

print(dev1.firstname, dev1.printfullname(), dev1.language)


    