#  i want the user to input the amount of grades there are then add them to an array take an average of the grades and list the average and all grades

gradeCount = int(input("How many grades do you have? "))
gradeArr = []
gradeTotal = 0

for grade in range(0,gradeCount,1):
    inputGrade = float(input("Please enter your grade: "))
    gradeArr.append(inputGrade)
for grade in gradeArr:
    gradeTotal = grade + gradeTotal
gradeAverage = gradeTotal / gradeCount
print("Your average is: ", gradeAverage,"%")
print("grades: ")
for grade in gradeArr:
    print(grade, "%")