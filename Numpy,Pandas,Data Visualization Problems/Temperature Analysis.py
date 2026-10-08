import numpy as np

temperature = np.array([28, 31, 29, 32, 34, 30, 33])

average = np.mean(temperature)
highest = np.max(temperature)
lowest = np.min(temperature)

print("Temperature:", temperature)
print("Average Temperature:", average)
print("Highest Temperature:", highest)
print("Lowest Temperature:", lowest)

print("Temperatures above 30°C:", temperature[temperature > 30])

updated_temperature = temperature + 2

print("Updated Temperature:", updated_temperature)
