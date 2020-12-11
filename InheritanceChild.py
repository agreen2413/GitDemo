from OOPS import CalculateData  #In Java you declare import and the name of the class, in Python you use from to import class.


class ChildInheritance(CalculateData): #In Python, by passing the class "CalculateData" as a parameter in the class "ChildInheritance" this is called "Inheritance"
    num2 = 200

    # Default Constructor
    def __init__(self):  # In Python this is how you declare constructor w/ keyword init. self is c global variable
        CalculateData.__init__(self, 5, 5)

    def getCompleteData(self):       # A method
        return self.num2 + self.num + self.Summation()

obj = ChildInheritance()
print(obj.getCompleteData())
