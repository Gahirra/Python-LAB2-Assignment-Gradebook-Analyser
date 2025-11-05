# GradeBook Analyzer,Name: Gahirra Kaur ,Date: 1/11/2025

print("Welcome to the GradeBook Analyzer!")
marks = {}

num = int(input("How many students? "))

for i in range(num):
    name = input("Enter student name: ")
    score = float(input("Enter marks: "))
    marks[name] = score

average = sum(marks.values()) / len(marks)
max_score = max(marks.values())
min_score = min(marks.values())
print("\nAverage marks:", average)
print("Highest marks:", max_score)
print("Lowest marks:", min_score)

grades = {}

for name , score in marks.items():
    if score >= 90:
        grades[name] = 'A'
    elif score >= 80:
        grades[name] = 'B'
    elif score >= 70:
        grades[name] = 'C'
    elif score >= 60:
        grades[name] = 'D'
    else:
        grades[name] = 'F'


print("\nName\tMarks\tGrade")
print("-----------------------")

for name in marks:
    print(name, "\t", marks[name], "\t", grades[name])


passed = [name for name, score in marks.items() if score >= 40]
failed = [name for name, score in marks.items() if score < 40]

print("\nPassed Students:", passed)
print("Failed Students:", failed)