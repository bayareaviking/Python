# 2. Use open and close functions to work with a file
# File used in this demo
the_file = 'files/people.csv'

# Open a file for reading
with open(the_file, "r") as file:
    # Here is where operations are performed, for example reading from the file or getting some information
    print("This file is called: " + file.name) 
    print("It uses the following encoding: " + file.encoding)
    print("It was opened in the following mode: " + file.mode)
    print("Is '" + the_file +"' closed? -> " + str(file.closed))

# Always close the file, or else bad things may happen
print("Is '" + the_file +"' closed? -> " + str(file.closed))
print("Did you notice I never called 'close'?")
print()
