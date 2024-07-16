import os
import shutil
from pathlib import Path

# Get current working directory
current_dir = os.getcwd()
print(current_dir)

# os contains path-specific functionality
# Can get an absolute path from a relative one
print(os.path.abspath('./..'))
# Backslashes require escaping
print(os.path.abspath('.\\..'))

# List contents of current directory
files_in_dir = os.listdir(current_dir)
print(files_in_dir)

# Create a new directory (can create multiple with mkdirs)
os.mkdir("pluralsight")

# Copy files using shutil
shutil.copytree("./code", "./pluralsight/code")
# Can rename with shutil.move or os.rename
shutil.move("./pluralsight/code", "./pluralsight/my_code")

# Change directory and confirm change
os.chdir("pluralsight")
current_dir = os.getcwd()
print(current_dir)
print(os.listdir("./my_code"))

# Change to parent directory
os.chdir("./..")
current_dir = os.getcwd()
print(current_dir)

# Delete directory, us rmdir if it is an empty directory
try:
    os.rmdir("./pluralsight")
except:
    print("Cannot delete a non-empty directory using os.rmdir, instead use shutil.rmtree")

# Delete a directory and all of its contents with shutil.rmtree
shutil.rmtree("./pluralsight")
print(os.listdir("."))

print(shutil.which("python-working-files/m2/slides-m2.pptx"))

# pathlib provides functionality to work with paths across multiple operating systems
path = Path("./python-working-files/m2/slides-m2.pptx")

# Get the file name
print(path.name)

# Get the directory
print(path.parent)

# Create a path 
new_path = path / "samples" / "README.MD"
print(new_path)

# List files with a specific condition
current_path = Path(".")
for file in current_path.glob("./python-working-files/m2/*.tscproj"):
    print(file)

print()