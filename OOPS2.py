# self keyowrd is mandatory for calling variable names into method
# instance and class variables have whole different purpose
# Constructor name should be __init__
# The "new" keyword is not required when you create a new obj in Python unlike in C# or Java

class CalculateData:
    num = 100

    #Default Constructor
    def __init__(self, a, b):  # In Python this is how you declare constructor w/ keyword init. self is c global variable
        self.firstInt = a
        self.secInt = b
        print("init is called automatically when obj is created")

    def getData(self):
        print("Executing method in class")


    def Summation(self):
        return self.firstInt + self.secInt + self.num  #or you can use self.num or CalculateData.num is valid too but NOT num.

# In Python, if your at this level of indentation, you are outside of this class already. Python is base on indentation
# and not bracket {} like in Java and C#
# In Python if you want to call the  method in the class, you dont need to declare the keyword "new". You just call the
# class CalculateData.

obj = CalculateData(2, 3)  #As you see we "dont" have the "new" keyowrd like we do in C# and Java obj = new CalculateData()
obj.getData()
print(obj.Summation())

obj1 = CalculateData(5, 5)  #As you see we "dont" have the "new" keyowrd like we do in C# and Java obj = new CalculateData()
obj1.getData()
print(obj1.Summation())