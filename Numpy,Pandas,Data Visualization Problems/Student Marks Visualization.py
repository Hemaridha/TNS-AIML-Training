import matplotlib.pyplot as plt

students = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

marks = [85, 72, 90, 45, 78, 88, 35, 65, 55, 92]

# Bar Chart
plt.figure(figsize=(8, 5))

plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()


# Performance Categories

excellent = 0
good = 0
average = 0
needs_improvement = 0

for mark in marks:
    if mark >= 80:
        excellent += 1
    elif mark >= 60:
        good += 1
    elif mark >= 40:
        average += 1
    else:
        needs_improvement += 1

categories = ["Excellent", "Good", "Average", "Needs Improvement"]
counts = [excellent, good, average, needs_improvement]

# Pie Chart
plt.figure(figsize=(7, 7))

plt.pie(counts, labels=categories, autopct="%1.1f%%")

plt.title("Student Performance Distribution")

plt.show()
