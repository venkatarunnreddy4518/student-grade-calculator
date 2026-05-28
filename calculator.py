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

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
    
def print_report():
    print("\n--- GRADE REPORT ---")
    for s in students:
        grade = calculate_grade(s["marks"])
        print(f"{s['name']} | Marks: {s['marks']} | Grade: {grade}")

print_report()