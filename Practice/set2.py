import json
import os
import pandas as pd
import matplotlib.pyplot as plt


path = "./set2.json"

if not os.path.exists(path):
    raise FileNotFoundError("File is not found")

df = None

with open(path, "r") as file:
    data = json.load(file)
    df = pd.DataFrame(data)

print(df)
course_counts = df["course_name"].value_counts()

print(course_counts)

# Create the bar plot
plt.bar(x=course_counts.index, height=course_counts.values)
plt.xlabel("Course Name")
plt.ylabel("Number of Enrollments")
plt.title("Enrollment Counts per Course")
plt.show()
