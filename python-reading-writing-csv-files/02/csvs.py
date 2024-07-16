import os
os.getcwd()
filename = 'some_text.txt'

# Open to read initial content
f = open(filename, 'r')
print(f.read())

# Open file and write an appended line
f = open(filename, 'a')
f.write("\n\nShave and a haircut, two bits!")

print()
print()

# Re-open file (last operation put you at EOL) and read
f = open(filename, 'r')
print(f.read())

f.close()