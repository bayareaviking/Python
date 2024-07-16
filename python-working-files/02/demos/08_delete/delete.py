import os
import shutil

folder = "sample_files"
python_sample = "sample_files/python_sample.txt"

# Create a directory
os.mkdir(folder)

# Create a file in the directory
with open(python_sample, "w") as f:
    f.write("Hello, world!")

# Delete the file
os.remove(python_sample)

# Delete the directory (must be empty)
os.rmdir(folder)

# Recreate the directory and file
# Create a nested directory structure that contains the group of directories
directories = "2023/02/28"
a_file = "pythonCode.txt"

os.makedirs(directories)
with open(os.path.join(directories, a_file), "w") as f:
    f.write("Hello, world!")


# Delete the directory and all its contents
shutil.rmtree("2023")
print()