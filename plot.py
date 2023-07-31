import matplotlib.pyplot as plt
import random

# Creating a new figure and axes
fig, ax = plt.subplots()

# X-axis values (1 to 10)
x_values = list(range(1, 11))

# Plotting the random numbers
ax.plot(x_values, random_numbers, marker='o', linestyle='-', color='b')
ax.set_xlabel('Index')
ax.set_ylabel('Random Numbers')
ax.set_title('Plot of Random Numbers')
ax.grid(True)
#plt.show()

# Displaying the plot
fig