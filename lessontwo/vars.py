myint = 7
myfloat = 7.0 # you can do floats with a .0 type numb OR FLOAT(7)
myfloat1 = float(8)
mystring = "string" #items with "" around them are assigned as strings

print(myfloat,myint) # will print 7.0 7

x, y = 2,3 # will assign x=2 y=3
print(x,y) # prints 2 3

print(mystring, x) # you can mix strings and numbers 
#print(mystring + x + y) this however will not work because you can add numbers to strings and vice versa
print(x + y) # this will print 5 
print(x,"+",y, "equals" ,(x + y) ) #because the x+y is in (  ) it will work prints 2 + 3 equals 5
print(x,"+",y, "equals" ,x + y) #BUT this will also work, as long as its not two mismatched types

# change this code
#mystring = None this gives it no value
#print(umyfloat) # will print "none"
# testing code


umystring = "hello"
umyfloat = float(10)
umyint = 20

if mystring == "hello": #matches
    print("String: %s" % umystring)
if isinstance(umyfloat, float) and myfloat == 10.0:
    print("Float: %f" % umyfloat)
if isinstance(myint, int) and umyint == 20:
    print("Integer: %d" % umyint)
# if all match it will print out the bottom print line, but if one is missing it wont print anything


#############LISTS##############

mylist =[1,2,3] # it indexs at 0,1 2 so 0 =1, 1=2 ect
print(mylist[1]) #prints 2
print(mylist[2]) #prints 3
#print(mylist[3]) will fail


###practice###
numbers = [] #blank
strings = []
names = ["john","eric", "jessie"]

numbers.append(1) #append to add numbers to list
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]

print(numbers) #[1,2,3]
print(strings) #['hello', 'world']
print("the second name on the list is %s" % second_name)
#using the %s opperator inside the string with %second_name on the tail
#it will fill in the & for the var provided
#the second name on the list is eric is the result