import matplotlib.pyplot as plt

days = ["Thur", "Fri", "Sat", "Sun"]
bills = [150, 120, 250, 190]

plt.bar(days, bills)
plt.title("Bar Chart")
plt.xlabel("Days")
plt.ylabel("Bills")
plt.show()