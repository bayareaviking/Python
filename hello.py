""" 
def greeting(name):
    print(f"Hello, {name}!")

inputName = input("Enter your name: ")
greeting(inputName)
 """
def greeting(name):
    return f"Hello, {name}!"\

def main():
    inName = input("Enter your name: ") # If main() is not defined, this variable would be GLOBAL

main()

