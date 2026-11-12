# Normal arguments and *args

def student(name, *subjects):
    print(f"Student_name: {name}")
    print("Subjects enrolled: ")
    print(".............")
    
    for subject in subjects:
        print(subject)

student("sammy", "maths", "history", "computer")