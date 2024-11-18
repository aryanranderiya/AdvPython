import matplotlib.pyplot as plt
import numpy as np

# Data for the plot
teams = ["Team A", "Team B", "Team C", "Team D", "Team E"]
boys = [25, 30, 35, 40, 20]
girls = [20, 25, 30, 35, 15]

plt.bar(teams, height=boys, color="blue", label="Boys")
plt.bar(teams, height=girls, bottom=boys, color="pink", label="Girls")

plt.xlabel("Teams")
plt.ylabel("Contribution")
plt.title("Contribution of Boys and Girls in the Teams")
plt.legend()
plt.show()
