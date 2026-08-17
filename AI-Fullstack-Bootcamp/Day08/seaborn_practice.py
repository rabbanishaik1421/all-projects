import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("tips.csv")
df = pd.DataFrame(data)
# print(df)

# sns.lineplot(x="sex", y="total_bill", data=df)
# plt.title("Line Chart")

# sns.barplot(x="day", y="tip", data=df)
# plt.title("Bar Plot")

sns.scatterplot(x="day", y="tip", data=df)
plt.title("Scatter Plot")
plt.show()
