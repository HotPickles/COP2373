import csv

def store_grades():
    #asks the instructor for the student count and stores it
    student_count = int(input("How many students would you like to enter? "))

    #write in the file
    with open('grades.csv', mode='w') as file:
        writer = csv.writer(file)

        #get the exam grades for multiple students with the loop
        for student in range(student_count):
            print(f"\nEntering data for student #{student + 1}:")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            exam1 = int(input("Exam 1 Grade: "))
            exam2 = int(input("Exam 2 Grade: "))
            exam3 = int(input("Exam 3 Grade: "))

            #writes name/grade data
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

def read_grades():
    #makes the header
    print(f"\n{'First Name':<25} {'Last Name':<25} {'Exam 1':25} {'Exam 2':25} {'Exam 3':25}")

    #opens the csv file to read it
    with open('grades.csv', mode='r') as file:
        reader = csv.reader(file)

        for row in reader:
            #needed to prevent a crash from an empty line
            if row:
                first, last, e1, e2, e3 = row
                print(f"{first:<25} {last:<25} {e1:25} {e2:25} {e3:25}")
            else:()

#calls the functions to run the program
store_grades()
read_grades()