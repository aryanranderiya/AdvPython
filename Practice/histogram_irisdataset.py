import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
species = iris["species"].unique()
fig, axes = plt.subplots(1, 5)

for ax, sp in zip(axes, species):
    ax.hist(iris.loc[iris["species"] == sp, "sepal_length"], bins=15)
    ax.set_title(f"Sepal Length - {sp.capitalize()}")

plt.show()
