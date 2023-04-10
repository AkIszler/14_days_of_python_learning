class MyClassDemo:
    variable1 = "hello world" #adds string to class variable

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClassDemo()
myobjecty = MyClassDemo()
myobjecty.variable2 = "goodbye world" #adds string to variable2 under the class MyClassDemo

print(myobjectx.variable1) # "hello world"
print(myobjecty.variable2) # prints "goodbye world"

class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber()) #Prints '7'


# final exercise

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car1.name = "fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60_000.00

car2 = Vehicle()
car2.name = "jump"
car2.color = "blue"
car2.kind = "Van"
car2.value = 100_000.00

# test code
print(car1.description())
print(car2.description())