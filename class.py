class employee:
    def __init__(self,name,dob,town):
        self.name = name
        self.dob = dob
        self.town = town
        
    def printemployeedetails(self):
        details_print = (f"name is {self.name} and the town is {self.town} and dob is {self.dob}")
        return details_print
    
    
class developer(employee):
    