# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age)) # %s and %d are placeholders for strings and integers respectively.

if name == "John" and age == 23: #an example of a conditional statement.
    print("John is 23.") #using indents to block the code.

mylist = [1,2,3]
print("A list: %s" % mylist) #an example of a list using a placeholer

#%s - String (or any object with a string representation, like numbers)

#%d - Integers

#%f - Floating point numbers

#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
myfloat = 7.02352
print("the answer is %.3f" % myfloat) 
#an example of a floating point number using a placeholer 
#the .3f is the number of digits to the right of the decimal.

#%x/%X - Integers in hex representation (lowercase/uppercase)
i = 678
h = format(i, '#x')
print("the number is" , h) #prints out hex rep of i in lowercase

#example of using a placeholder to print out a list of strings and numbers
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
#using the %s which shows String (or any object with a string like numerical items
print(format_string % data)

#more basic operations

astring = "hello world"
astring2 = "hello people"

print(len(astring)) #will print out the lenth (lens) of the string this includes spaces.
print(astring[0]) #will print out the first letter of the
print(astring[-1]) #will print out the last letter of the string.
print(astring2.index("p")) #this will print out the index of the first "p" in the string.
print(astring.count("l")) #this will print out the number of "l" in the string. in this case 3 'l's
print(astring[3:7]) #will print out the string from the 3rd to the 7th letter.

print(astring[3:7]) #will print out lo w
print(astring[3:7:1]) # this will also print lo w This is extended slice syntax. The general form is [start:stop:step].

##############CONDITONS##################

x = 2

#print(x == 2)  # this will print true
#print(x == 4)  # this will print false
#print((x *3) == 6) # this will print true

x = 2
print(x == 2) and (x == 4) # this will prints true for some reason
print(x == 2) or (x == 4) # this will print true 

if (x == 2) and (x == 4):
    print("x is 2 and 4")
