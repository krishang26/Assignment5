student_marks={
    "Alice":85,
    "Rakesh":70,
    "Ram":78,
    "Bob":90,
    "Shyam":89,
}
name=input("Enter your name:")
if name in student_marks:
    print("Marks of the student:", student_marks[name])
else:
    print("Student name is not available")



