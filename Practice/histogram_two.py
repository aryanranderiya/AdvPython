import matplotlib.pyplot as plt
import pandas as pd

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5]

df = pd.DataFrame(
    {
        "DatasetA": a,
        "DatasetB": b,
    }
)

plt.hist(
    df["DatasetA"], color="red", alpha=0.5, bins=5, edgecolor="black", label="Dataset A"
)
plt.hist(
    df["DatasetB"],
    color="green",
    alpha=0.5,
    bins=5,
    edgecolor="black",
    label="Dataset B",
)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()
