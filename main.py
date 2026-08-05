from gradebook import *

students=load_students()
while True:
    print("\n1.Add Student\n2.Add Score\n3.View Students\n4.Statistics\n5.Save\n6.Exit")
    c=input("Choice: ")
    if c=="1":
        add_student(students,input("Name: "))
    elif c=="2":
        n=input("Student: ")
        if n in students:
            add_score(students,n,float(input("Score: ")))
    elif c=="3":
        for n,s in students.items():
            avg=calculate_average(s)
            print(n,s,"Average",avg,"Grade",letter_grade(avg))
    elif c=="4":
        print("Class average:",class_average(students))
    elif c=="5":
        save_students(students); print("Saved.")
    elif c=="6":
        save_students(students); break
