fileName = "02/demos/07_read_write/loremipsum.txt"

# Open a file for reading and then close
lif = open(fileName, "r")
li_lines = lif.read()
print(li_lines)
lif.close()


# Use a context manager, which means there is no need to close
with open(fileName, "r") as f:
    contents = f.read()
    print(contents)


# Use a context manager, which means there is no need to close
with open(fileName, "a") as f:
    f.write("Last line")    

print()
