filew = open("test.txt", "w") # 'w' means 'write' mode and will overwrite the file if it exists
# you can also use 'a' to append to an existing file which will append to the end of the file(add on to the end of the file)
filew.write("This is a test file") # this will write a string to the file. 

filew.close() # this will close the file 
#ALWAYS CLOSE THE FILE
# If you want to write and than read the file, you need to close the file first

# this will create a file called 'test.txt' in the same directory as the python script
# it will write the test file string and than close the file
fread = open("test.txt", "r")
print(fread.read())

filew.close() # close the file

filew = open("test.txt", "a") # 'a' means 'append' mode 
filew.write("this is another line") # this will write a string to the file. 
filew.close() # this will close the file



print(fread.read())