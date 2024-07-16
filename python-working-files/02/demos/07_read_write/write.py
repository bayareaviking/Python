filename = "file_for_writing.txt"


# Open the file in write mode
file = open(filename, "w")
# Write data to the file
file.write("This is the first line in the file.\n")
# Close the file
file.close()


# Open the file in write mode, again... which overwrites the file
file = open(filename, "w")
# Write data to the file
file.write("This is a new line in the file.\n")
# Close the file
file.close()


# Open the file in append mode
file = open(filename, "a")
# Write data to the file
file.write("This is an appended line in the file.\n")
# Close the file
file.close()


# Open the file in write mode (and overwrite the contents of the file)
file = open(filename, "w")
# Write multiple lines to the file
file.writelines(["Hello! \nThis is the second line", "\nSee you soon!"])
# Append multiple lines of text using writelines and a list
# Important to include the newline character \n at the end of each line of text, as writelines does not add it automatically
lines = ["This is line 3\n", "This is line 4\n", "This is line 5\n"]
file.writelines(lines)
# Append multiple lines of text using writelines and a generator expression
file.writelines(f"This is line {i}\n" for i in range(6, 9))
# Close the file
file.close()
print()

