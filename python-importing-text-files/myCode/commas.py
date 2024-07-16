#from pprint import pprint 
import csv

the_file = 'files\people.csv'

# Open the file and read
with open(the_file, newline='') as csvfile:
    person = csv.reader(csvfile, delimiter=',', quotechar='"')

    # Skip header row
    next(person)

    #pprint the records
    for row in person:
        print(row)