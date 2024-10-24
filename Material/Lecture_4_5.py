
# 1. CSV File Handling for Student Grades
import csv

input_file = "student_grades.csv"
output_file = "student_average_grades.csv"
student_grades = {}

with open(input_file, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row["Name"]
        math_score = int(row["Maths"])
        science_score = int(row["Science"])
        english_score = int(row["English"])
        scores = [math_score, science_score, english_score]
        average_score = sum(scores) / len(scores)
        student_grades[name] = average_score

with open(output_file, "w", newline="") as csvfile:
    fieldnames = ["Name", "Average"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for name, average in student_grades.items():
        writer.writerow({"Name": name, "Average": average})

print("Successfully calculated and saved average grades in 'student_average_grades.csv'.")

# 2. Using pandas to Process CSV Data
import pandas as pd

calculate_average = lambda scores: sum(scores) / len(scores)

def main():
    input_file = "student_grades.csv"
    df = pd.read_csv(input_file)
    df["Average"] = df.apply(lambda row: calculate_average([row["Maths"], row["Science"], row["English"]]), axis=1)
    df.to_csv(input_file, index=False)

    print("Successfully calculated and appended average grades as a new column in 'student_grades.csv'.")

if __name__ == "__main__":
    main()

# 3. Using Lambda Functions with Map
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared Numbers:", squared_numbers)

# 4. Using Lambda Functions with Filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# 5. Using Reduce to Find the Maximum Value
from functools import reduce
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print("Maximum Value:", max_value)

# 6. Sum of Squares Using Map and Reduce
sum_of_squares = reduce(lambda x, y: x + y, map(lambda x: x ** 2, numbers))
print("Sum of Squares:", sum_of_squares)

# 7. Filtering Strings by Length
words = ['apple', 'banana', 'cherry', 'date']
long_words = filter(lambda word: len(word) > 5, words)
print("Long Words:", list(long_words))

# 8. Converting Celsius to Fahrenheit Using Map
celsius = [39.2, 45.5, 67.9, 38.3]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("Fahrenheit Temperatures:", fahrenheit)
