# File used in this demo.
the_file = 'files/people.csv'

# Open the file for reading.
file = open(the_file, "r")

# Read the file using readlines
lines_array = file.readlines()

for line in lines_array:
    each_line = line.split(sep=',')
    print(each_line[0])

print()