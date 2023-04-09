import time

class MyClass:
    variable = "Yay pizza"
    print(variable)

    def function(self):
        print("I like my pizza, because pizza is my favorite food")

class foodClass: # class for talking to user
    #get class set
    function = MyClass.function
    function(self=MyClass)
    #gran their fav food with the variable "their"
    their = input("what is your favorite food? ")
    print("interesting........")
    print("let me think")
    #do a stupid wait for lulz
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)

    print("fine........")
    time.sleep(2)
    print ("I guess %s is an okay food" % their)

    