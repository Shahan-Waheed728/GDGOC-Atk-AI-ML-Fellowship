# python program to use dictionary and list for adding and updating student record
students = []
def add_student():
    roll_no = int(input("Enter roll-no: "))
    for student in students:
        if student[roll_no] == roll_no:
            print("Student with this roll-no already exists.")
            return
    name = input("Enter student name: ")
    marks = float(input("Enter obtained marks :"))
    status = input("Enter status: ")

    student = {
        "roll-no" : roll_no,
        "name" : name,
        "total_marks" : 520,   
        "obtained_marks" : marks,
        "status" : status
    }
    students.append(student)
    print("Student added successfully!")

def update_student():
    roll_no = int(input("Enter roll-no of student to update: "))
    for student in students:
        if student["roll-no"] == roll_no:
            print(f"Updating record for {student['name']}")
            student["name"] = input("Enter new name: ") or student["name"]
            student["total_marks"] = float(input("Enter new total marks: ") or student["total_marks"])
            student["obtained_marks"] = float(input("Enter new obtained marks: ") or student["obtained_marks"])
            student["status"] = input("Enter new status: ") or student["status"]
            print("Student record updated!")
            return
    print("Student not found!")

def display_students():
    print("\n---All Student Records---")
    for student in students:
        print(student)

# Main program
while True:
    print("\n1. Add Student")
    print("2. Update Student")
    print("3. Display Students")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_student()
    elif choice == "3":
        display_students()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")