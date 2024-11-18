import matplotlib.pyplot as plt

data = {"C": 20, "C++": 15, "Java": 30, "Python": 35}
plt.bar(data.keys(), data.values())
plt.xlabel("Subjects")
plt.ylabel("Students")
plt.title("Students enrolled in different courses")
plt.show()
