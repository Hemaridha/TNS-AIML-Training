import pandas as pd

data = {
    "Name": ["Arun", "Priya", "Rahul", "Divya", "Karthik", "Anu", "Vijay", "Meena"],
    "Department": ["CSE", "ECE", "CSE", "IT", "ECE", "CSE", "IT", "CSE"],
    "Marks": [85, 72, 90, 65, 78, 88, 70, 82],
    "Attendance": [90, 85, 95, 75, 88, 92, 78, 80]
}

df = pd.DataFrame(data)

print("First 5 Students:")
print(df.head())

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nStudents who scored more than 75:")
print(df[df["Marks"] > 75])

print("\nStudents whose attendance is below 80%:")
print(df[df["Attendance"] < 80])

print("\nStudents sorted by Marks:")
print(df.sort_values("Marks"))
