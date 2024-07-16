
the_file = "files\\badges-five-header.txt"

with open(the_file, "r") as file:
    print("The name of the file is " + file.name)
    print()
    content = file.read()
    print(content)
    print() 
    
    # The last print() function stopped at EOF
    # Go back to beginning of file
    file.seek(0)

    # Then print
    print("Printing lines in the file, one by one")
    for line in file:
        print(line)
    file.seek(0)



    