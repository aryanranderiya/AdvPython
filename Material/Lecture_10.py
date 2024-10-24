
import os
import shutil
from pathlib import Path

# 1. Get the current working directory
cwd = os.getcwd()
print("Current working directory:", cwd)

# 2. Change Directory
# Uncomment and provide a valid path to test changing directory
# os.chdir('/path/to/directory')
# print("Changed directory to:", os.getcwd())

# 3. List Files and Directories
files_and_dirs = os.listdir()
print("Files and directories:", files_and_dirs)

# 4. Create a Directory
os.makedirs('new_directory', exist_ok=True)
print("Directory 'new_directory' created")

# 5. Create a File
with open('new_file.txt', 'w') as file:
    file.write("This is a new file.")
print("File 'new_file.txt' created")

# 6. Delete a File
os.remove('new_file.txt')
print("File 'new_file.txt' deleted")

# 7. Delete an Empty Directory
os.rmdir('new_directory')
print("Directory 'new_directory' deleted")

# 8. Delete a Directory with Contents
# Uncomment to test deleting a directory with contents
# shutil.rmtree('directory_with_contents')
# print("Directory 'directory_with_contents' and its contents deleted")

# 9. Move a File or Directory
# Uncomment to test moving a file or directory
# shutil.move('source_file.txt', 'destination_directory/')
# print("File moved to destination directory")

# 10. Using pathlib for Object-Oriented File Handling
path = Path('new_directory')
path.mkdir(parents=True, exist_ok=True)
print(f"Directory {path} created")

# 11. Iterating Over Directory Contents
for item in path.iterdir():
    print(item)

# 12. Delete a File or Directory with pathlib
file_path = Path('new_file.txt')
if file_path.exists():
    file_path.unlink()
    print(f"File {file_path} deleted")

if path.exists():
    path.rmdir()
    print(f"Directory {path} deleted")

# 13. Check if a File or Directory Exists
path = Path('some_directory_or_file')
if path.exists():
    print(f"{path} exists")
else:
    print(f"{path} does not exist")

# Task: List all files and directories in the current working directory
files = []
directories = []
for item in os.listdir(cwd):
    if os.path.isfile(item):
        files.append(item)
    elif os.path.isdir(item):
        directories.append(item)
print("Files:", files)
print("Directories:", directories)
