import csv
import numpy as np

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


def analyze_grades():
    #makes a list out of the csv
    list = []
    with open('grades.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                #does the changing of being a string in the list to an interger
                list.append([int(row[2]), int(row[3]), int(row[4])])

    #turns the list into an array
    data = np.array(list)


    #prints the dataste structure
    print("dataset structure:")
    print(data)

    #prints the statistics arrays
    print("mean per exam:")
    print(np.mean(data, axis=0))
    print("median per exam:")
    print(np.median(data, axis=0))
    print("standard deviation per exam:")
    print(np.std(data, axis=0))
    print("minimum for each exam:")
    print(np.min(data, axis=0))
    print("maximum for each exam:")
    print(np.max(data, axis=0))

    #print the overall statistics arrays
    print("overall mean:")
    print(np.mean(data))
    print("overall median:")
    print(np.median(data))
    print("overall standard deviation:")
    print(np.std(data))
    print("highest score:")
    print(np.max(data))
    print("lowest score:")
    print(np.min(data))

    #analyzes passing standing of students
    passed = np.sum(data >= 60, axis=0)
    failed = np.sum(data < 60, axis=0)
    print("passed each exam:")
    print(passed)
    print("failed each exam:")
    print(failed)

    #caclulates % that passed
    pass_percent = (np.sum(data >= 60) / data.size) * 100
    print("overall pass percentage:")
    print(pass_percent)

#calls the running code
store_grades()
read_grades()
analyze_grades()