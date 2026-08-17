import matplotlib.pyplot as plt

cars = ["Audi", "BMW", "Suzuki", "Hyundai", "Tata"]
data = [20, 13, 27, 22, 19]

plt.pie(data, labels=cars, autopct="%1.1f%%")
plt.title("Pie chart")
plt.show()