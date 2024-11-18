import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])

plt.hist(df, bins=[0, 70, 95, 97, 100])
plt.title("Sax sux")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.legend()
plt.show()
