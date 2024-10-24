
# Handling ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Handling FileNotFoundError
try:
    with open("xyz.txt", "r") as file:  # Assumes file does not exist
        content = file.read()
except FileNotFoundError:
    print("File not found.")

# Handling TypeError
try:
    result = 10 + "5"
except TypeError:
    print("Type mismatch: Cannot add integer and string.")

# Handling ValueError
try:
    number = int("Hello")
except ValueError:
    print("Value error: Cannot convert string to integer.")

# Handling IOError
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except IOError:
    print("IO error: File not found.")

# Handling IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Index error: Index out of range.")

# Handling KeyError
try:
    my_dict = {"name": "John", "age": 30}
    print(my_dict["gender"])
except KeyError:
    print("Key error: 'gender' key not found in dictionary.")

# Handling NameError
try:
    print(x)
except NameError:
    print("Name error: x is not defined.")

# Custom FileNotFoundError Example
class FileNotFoundError(Exception):
    def __init__(self, filename):
        self.filename = filename
    def __str__(self):
        return f"{self.filename} not found in the directory."

def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    except IOError:
        raise FileNotFoundError(filename)

if __name__ == "__main__":
    try:
        read_file("example.txt")
    except FileNotFoundError as e:
        print(e)

# Comprehensive try-except-else-finally Example
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero.")
except ValueError:
    print("ValueError: Please enter a valid integer.")
else:
    print("No exceptions occurred.")
finally:
    print("Execution completed, regardless of error occurrence.")

# Handling Multiple Exceptions
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except (IndexError, KeyError):
    print("An IndexError or KeyError occurred.")
