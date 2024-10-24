M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Access the second row of the matrix
print(M[1])  # Output: [4, 5, 6]

# Get the number of rows in the matrix
print(len(M))  # Output: 3

# Create a set from the matrix
S = {tuple(row) for row in M}
print(S)  # Output: {(1, 2, 3), (4, 5, 6), (7, 8, 9)}

# Access the element at the second row, first column
N = M[1][0]
print(N - 20)  # Output: -16

# Create a list with an initial element
y = [20]

# Append a list to the existing list
y.append([3, 4, 5])
print(y)  # Output: [20, [3, 4, 5]]

# Extend the existing list with individual elements
y.extend([3, 4, 5])
print(y)  # Output: [20, [3, 4, 5], 3, 4, 5]

# Create a list of prime numbers
primes = [2, 3, 5, 7]
print(primes)





# Create a list of planets
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets)

# Create a list of lists
hands = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(hands)

# Create a list with mixed data types
my_list = ['abc', 14, True, 40, 'sale']
print(my_list)

# Create a list with duplicate elements
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# Get the length of the list
print(len(thislist))

# Check the data type of the list
print(type(thislist))

# Create a list using the list() constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)




# Access individual list elements
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets[0])  # Output: Mercury
print(planets[-1])  # Output: Neptune

# Slicing
print(planets[0:3])  # Output: ['Mercury', 'Venus', 'Earth']
print(planets[:3])  # Output: ['Mercury', 'Venus', 'Earth']
print(planets[3:])  # Output: ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets[1:-1])  # Output: ['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus']
print(planets[-3:])  # Output: ['Saturn', 'Uranus', 'Neptune']

# Slicing with step
print(planets[::2])  # Output: ['Mercury', 'Earth', 'Jupiter', 'Uranus']
print(planets[::-1])  # Output: ['Neptune', 'Uranus', 'Saturn', 'Jupiter', 'Mars', 'Earth', 'Venus', 'Mercury']



# Modify a list by assigning to an index
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets[3] = 'Malacandra'
print(planets)  # Output: ['Mercury', 'Venus', 'Earth', 'Malacandra', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Append an element to a list
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Extend a list with elements from another list
cars = ['Ford', 'Volvo']
fruits.extend(cars)
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange', 'Ford', 'Volvo']





# Extend a list with elements from another list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

# Create a tuple using the tuple() constructor
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)  # Output: ('apple', 'banana', 'cherry')

# Access tuple elements
print(thistuple[1])  # Output: banana




# Check if an item exists in a tuple
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

# Convert a tuple to a list to change its values
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y[1] = "kiwi"
thistuple = tuple(y)
print(thistuple)

# Add items to a tuple by converting it to a list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)





# Create a dictionary
colorOfFruits = {"apple": "red", "mango": "yellow", "orange": "orange"}

# List all keys
print(colorOfFruits.keys())  # Output: dict_keys(['apple', 'mango', 'orange'])

# List all values
print(colorOfFruits.values())  # Output: dict_values(['red', 'yellow', 'orange'])

# List all items (key-value pairs)
print(colorOfFruits.items())  # Output: dict_items([('apple', 'red'), ('mango', 'yellow'), ('orange', 'orange')])

# Create a set
ages = {27, 24, 25, 26}
print(ages)  # Output: {24, 25, 26, 27}

# Add an element to a set (if it doesn't exist)
ages.add(23)
print(ages)  # Output: {23, 24, 25, 26, 27}

# Remove an element from a set
ages.remove(24)
print(ages)  # Output: {23, 25, 26, 27}

# Check if an element exists in a set
if 25 in ages:
    print("25 is in the set")  # Output: 25 is in the set





# Create a variable and assign a value
name = "snow storm"

# Access an element of a list using indexing
name[5] = "x"
print(name)  # Output: snow stxrm

# Nested loops
for i in range(5):
    for j in range(i):
        print(i, j)

# List slicing
my_list = [3, 4, 9, 1, 2, 6, 8]
print(my_list[1:4])  # Output: [4, 9, 1]
print(my_list[-6:-4])  # Output: [9, 1]
print(my_list[-1:3])  # Output: []
print(my_list[-1:4])  # Output: [8]
print(my_list[2:4])  # Output: [9, 1]

# While loop with list manipulation
A = [1, 2, 3, 7, 12, 34, 15, 18, 22]
i = 0
while i < len(A):
    if A[i] % 2 == 0:
        A.remove(A[i])
    else:
        i += 1
print(A)  # Output: [1, 3, 7, 12, 15, 18, 22]

# List comprehension
a = [i for i in range(20) if i % 2 == 0]
print(a)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]