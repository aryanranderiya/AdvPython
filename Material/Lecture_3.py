
# 1. Open and Close a File
f = open("test.txt")
f.close()
print("File opened and closed successfully.\n")

# 2. Writing to a File
fp = open("test.txt", 'w')
fp.write("my first file\n")
fp.write("This file\n\n")
fp.write("contains three lines\n")
fp.close()
print("Data written to test.txt successfully.\n")

# 3. Appending to a File
file1 = open("myfile.txt", "a")
file1.write("Hello eInfochips again\n")
L = ["This is Delhi\n", "This is Paris\n", "This is London\n"]
file1.writelines(L)
file1.close()
print("Data appended to myfile.txt successfully.\n")

# 4. Reading from a File
file1 = open("myfile.txt", "r")
print("Output of Read function is:")
print(file1.read())
file1.close()

# 5. Using `with` to Handle Files
with open("test.txt", 'w') as fp:
    fp.write("my first file\n")
    fp.write("This file\n\n")
    fp.write("contains three lines\n")
print("File handling with `with` for test.txt done successfully.\n")

# 6. Read Specific Lines from a File
file = open('filehandle.txt', "r")
content = file.readlines()
print("3rd line:")
print(content[2])
print("First three lines:")
print(content[0:3])
file.close()
