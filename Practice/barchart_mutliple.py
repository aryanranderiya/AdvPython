# Data for two regions
from matplotlib import pyplot as plt

region_1_sales = [50, 85, 90, 60, 30]
region_2_sales = [70, 65, 80, 95, 55]

bar_width = 0.35

products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
x_indexes = range(len(products))

plt.bar(x_indexes, region_1_sales, width=bar_width, color="skyblue", label="Region 1")
plt.bar(
    [x + bar_width for x in x_indexes],
    region_2_sales,
    width=bar_width,
    color="lightcoral",
    label="Region 2",
)
plt.title("Sales Comparison by Product and Region")
plt.xlabel("Products")
plt.ylabel("Number of Sales")
plt.xticks([x + bar_width / 2 for x in x_indexes], products)
plt.legend()
plt.show()
