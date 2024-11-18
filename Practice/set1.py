import pandas as pd
import os
from fpdf import FPDF
from datetime import datetime
import matplotlib.pyplot as plt

path = "./set1.csv"

if not os.path.exists(path):
    raise FileNotFoundError("File doesn't exist!")

df = pd.read_csv("./set1.csv")

bins = [18, 25, 35, 50, float("inf")]
labels = ["18-25", "26-35", "36-50", "51+"]
df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels, right=True)
age_group_summary = df.groupby("age_group", observed=True)["purchase_amount"]
total_purchase = age_group_summary.sum()
unique_customers = df.groupby("age_group", observed=True)["customerID"].nunique()
avg_purchase = age_group_summary.mean()

summary_df = pd.DataFrame(
    {
        "Total Purchase Amount": total_purchase,
        "Unique Customers": unique_customers,
        "Average Purchase Amount": avg_purchase,
    }
).reset_index()

pdf = FPDF()
pdf.add_page()
pdf.set_font(family="Helvetica", size=15)
pdf.cell(0, 10, "Welcome to Summary Statistics!", ln=True)
pdf.cell(0, 10, str(datetime.now()), ln=True)

pdf.set_font(family="Helvetica", size=13)
pdf.cell(30, 10, "Age Group", 1, 0, "C")
pdf.cell(55, 10, "Total Purchase Amount", 1, 0, "C")
pdf.cell(50, 10, "Unique Customers", 1, 0, "C")
pdf.cell(60, 10, "Average Purchase Amount", 1, 1, "C")

# print(summary_df)

for index, row in summary_df.iterrows():
    # pdf.cell(30, 10, str(row["age_group"]), 1, 0, "C")
    pdf.cell(30, 10, row["age_group"], 1, 0, "C")
    pdf.cell(55, 10, str(row["Total Purchase Amount"]), 1, 0, "C")
    pdf.cell(50, 10, str(row["Unique Customers"]), 1, 0, "C")
    pdf.cell(60, 10, str(row["Average Purchase Amount"]), 1, 1, "C")  # End of row


pdf.output("./test.pdf")

plt.pie(total_purchase, labels=labels)
plt.show()
