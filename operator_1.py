number = 1 + 2 * 3 /4
print(number) #prints 2.5

remainder = 11 % 3 #returns the integer remainder of the division
print(remainder) #prints 2

# to root numbers
squared = 7 ** 2 #it would be 7 squared 
cubed = 2 ** 3  #cubed
multip = 2 * 3 #basic multiplier is 6

print(squared) # prints 49
print(cubed) #8 
print(multip) #6

lotsofhello = "hello " * 20
print(lotsofhello) #prints hello 20 times

#lists with oper
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers) #prints [1,3,5,7,2,4,6,8]

print([1,2,3] * 3) # will print 1,2,3 3 times


#deeper dive

x = object()
y = object()


x_list = [x] * 10
y_list = [y] * 10
big_list = [x,y] *10

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")