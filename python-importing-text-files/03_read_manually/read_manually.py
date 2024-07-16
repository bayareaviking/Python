from pprint import pprint 


# 1. Use open and close functions to work with a file.

# File used in this demo.
the_file = 'files/people.csv'

# Open the file for reading.
file = open(the_file, "r")

# 2. Read the file using readlines
lines_array = file.readlines()

# Print line 2
print("Line 2: " + lines_array[2])

# Pretty-print the array
pprint(lines_array)

# Seek to start
file.seek(0)

# 5. Iterate over the file
for each_line in file:
    print(each_line)


# Always close the file, or else bad things may happen
file.close()
print()
