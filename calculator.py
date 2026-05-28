# Student Grade Calculator
print("Welcome to Grade Calculator")

students = []

def add_student(name, marks):
    students.append({"name": name, "marks": marks})
    print(f"Student {name} added!")

add_student("Alice", 85)
add_student("Bob", 72)
add_student("Charlie", 90)

print(students)