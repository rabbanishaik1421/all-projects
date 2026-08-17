# plt.lengend()

'''import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6], label='Sales')
plt.plot([1, 2, 3], [2, 4, 3], label='Expenses')

# Automatically detects and displays the 'Sales' and 'Expenses' labels
plt.legend() 
plt.show()'''

# plt.figure()
'''import matplotlib.pyplot as plt

# 1. Initialize the canvas with a custom size
plt.figure(figsize=(8, 5))

# 2. Add data to the active figure
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Sample Line Chart")

# 3. Render the window
plt.show()
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5)
y = x ** 2
plt.plot(x, y)

# 1. Set custom locations and text labels with a 45-degree rotation
plt.xticks(ticks=[0, 1, 2, 3, 4], labels=['Zero', 'One', 'Two', 'Three', 'Four'], rotation=45)

# 2. Get current locations and labels
locs, labels = plt.xticks()

# 3. Completely hide x-axis ticks
# plt.xticks([]) 

plt.show()
