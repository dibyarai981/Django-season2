def student():
    student = {}

    student["name"] = input("Enter your name: ")
    student["age"] = input("Enter your age: ")
    student["course"] = input("Enter your course: ")
    student["work"] = input("Enter your work")
    

    print("\nStudent Dictionary:")
    # print(student)
    return student

# Call the function
s1 = student()
s2 = student()
s3 = student()

print(s1,s2,s3)