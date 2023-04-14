########Dictionary########

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

#can also be written as:
phonebook2 = {
    "jack": 93837734264,
    "james": 5558675309,
    "April": 947662451
     }
print(phonebook2)

#iterate through the dictionary

myphonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in myphonebook.items():
    print("Phone number of %s is %d" % (name, number))

    #this will print out all the names and numbers in the dictionary
    #but in a more readable format
#deleting an entry

phonebook = {
   "Carl" : 938477566,
   "maxis" : 938377264,
   "carla" : 947662781
}
del phonebook["maxis"]

print(phonebook)

for name, number in phonebook.items():
    print("the numbers of %s and %s" % (name, number))

    #this will print out all the names and numbers in the dictionary
del phonebook["Carl"]

print(phonebook)    

# you can also use pop for removing an entry
phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
phonebook.pop("John",) #this will remove the "John" entry using pop
print(phonebook)


####exrcise ########Dictionary########

phonebook = {  
    "John" : 938477566,
    "Jack" : 938273444,
    "Jill" : 947662781
}  
# your code goes here
phonebook["Jake"]= 9382734443
del phonebook["Jill"]
# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")  