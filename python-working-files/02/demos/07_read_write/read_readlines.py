import os
from pprint import pprint 

fileName = "02/demos/07_read_write/loremipsum.txt"
os.system('cls') # Use 'clear' on Unix/Linux/MacOS


# Open the file in read mode and read all text
file = open(fileName, "r")
# Read the file
contents = file.read()
print(contents)
# Close the file
file.close()
os.system('cls')


# Open the file in read mode and read all text
file = open(fileName, "r")
# Read one line
line = file.readline()
print(line)
# Read another line
line = file.readline()
print(line)
# Close the file
file.close()
os.system('cls')


# Open the file in read mode and read all lines
file = open(fileName, "r")
# Read one line
line = file.readlines()
pprint(line)
# Close the file
file.close()
os.system('cls')


# Open a file for reading and try to write to the file
file = open(fileName, "r")
# Write data to the file
file.write("This is a new line in the file.\n")
# Close the file
file.close()


