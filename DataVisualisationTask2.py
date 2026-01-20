import pandas as pd

data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile", "Tablet"],
    "Sales": [50000, 30000, 20000, 55000, 32000, 25000],
    "Month": ["Jan", "Jan", "Jan", "Feb", "Feb", "Feb"]
}

df = pd.DataFrame(data)
df

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure()
sns.barplot(x="Product", y="Sales", data=df)
plt.title("Sales by Product")
plt.show()

plt.figure()
sns.lineplot(x="Month", y="Sales", hue="Product", data=df, marker="o")
plt.title("Monthly Sales Trend")
plt.show()

pivot = df.pivot("Product", "Month", "Sales")

plt.figure()
sns.heatmap(pivot, annot=True, fmt="d")
plt.title("Sales Heatmap")
plt.show()