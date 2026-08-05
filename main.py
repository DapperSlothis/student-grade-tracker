"""
main.py

This is the main program.

It displays the menu, accepts user input,
and calls functions from gradebook.py.
"""

from gradebook import *

# Load any previously saved students.
students=load_students()

# Keep displaying the menu until the user exits.
while True:
    print("\n1.Add Student\n2.Add Score\n3.View Students\n4.Statistics\n5.Save\n6.Exit")
    c=input("Choice: ")

    # Option 1 - Add a new student
    if c=="1":
        add_student(students,input("Name: "))

    # Option 2 - Add a score
    elif c=="2":
        n=input("Student: ")
        if n in students:
            add_score(students,n,float(input("Score: ")))

    # Option 3 - Display every student
    elif c=="3":
        for n,s in students.items():
            avg=calculate_average(s)
            print(n,s,"Average",avg,"Grade",letter_grade(avg))

    # Option 4 - Show class statistics
    elif c=="4":
        print("Class average:",class_average(students))

    # Option 5 - Save the data
    elif c=="5":
        save_students(students); print("Saved.")

    # Option 6 - Save and exit
    elif c=="6":
        save_students(students); break
