import numpy as np

marks = np.array([85, 72, 90, 65, 78, 88, 95, 70, 82, 60])

total = np.sum(marks)
average = np.mean(marks)
highest = np.max(marks)
lowest = np.min(marks)

print("Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

print("Marks greater than 75:", marks[marks > 75])
