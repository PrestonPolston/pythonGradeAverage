#  i want the user to input the amount of grades there are then add them to an array take an average of the grades and list the average and all grades

gradeCount = int(input("How many grades do you have? "))
gradeArr = []
highToLow = []
newHigh = 0
gradeTotal = 0
highGrade = 0
lowGrade = 100
j = 0


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

for grade in gradeArr:
    if (grade > highGrade):
        highGrade = grade
    if(grade < lowGrade):
        lowGrade = grade

print("Highest grade: ", highGrade)
print("Lowest grade: ", lowGrade)

for i in range(0, len(gradeArr), 1):
    if (j < len(gradeArr)):
        j = i + 1
    if gradeArr[j] > gradeArr[i]:
        newHigh = gradeArr[j]
        highToLow.append(newHigh)
        # gradeArr.pop(j)
        # newHigh = 0
        print(highToLow)



    