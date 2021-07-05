#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line

if __name__ == '__main__':

    gradebook = []
    student = []
    first = 100.0
    second = 100.0
    names = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        student.append(name)
        student.append(score)
        gradebook.append(student)
        student = []

    for i in gradebook:
        if i[1] <= first:
            if i[1] == first:
                first = i[1]
            else:
                second = first
                first = i[1]
        elif i[1] <= second:
            second = i[1]

    for j in gradebook:
        if j[1] == second:
            names.append(j[0])
    
    names.sort()

    for k in names:
        print(k)

