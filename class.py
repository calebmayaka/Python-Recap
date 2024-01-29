class employee:
    def __init__(self,name,dob,town):
        self.name = name
        self.dob = dob
        self.town = town
        
    def printemployeedetails(self):
        details_print = (f"name is {self.name} and the town is {self.town} and dob is {self.dob}")
        return details_print
    
    
class developer(employee):
    def __init__(self,name,dob,town,language):
        super().__init__(name,dob,town)
        self.language = language
    
name_input = str(input("Enter your full name: "))
dob_input = str(input("Enter your full name: "))
town_input = str(input("Enter your full name: "))
language_input = str(input("Enter your full name: "))


developer1 = developer(name_input,dob_input,town_input,language_input)

print(developer1.printemployeedetails())
    