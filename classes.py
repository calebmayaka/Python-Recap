#classes are likeblueprints to make multiple similar stuff
# for example a class can be created to be used to handle data of multiple employee
# a class is created using the class keyword

class employee:
    def __init__(self,firstname,lastname,dob,town):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.town = town
        
        
    def printfullname(self):
        print(self.firstname + self.lastname)
            

name1 = str(input("enter your first name: "))
name2 = str(input("enter your last name: "))
dobinput = int(input("enter your year of birth: "))
towninput = str(input("enter your town of residence: "))
employee1 = employee(name1,name2,dobinput,towninput)

print(employee1.firstname)

print(employee1.printfullname())