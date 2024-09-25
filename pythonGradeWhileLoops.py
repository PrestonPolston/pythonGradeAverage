# take an input of grades and go through the array using only while loops

numberOfGrades = int(input("How many grades do you have? "))
gradesCount = numberOfGrades
gradesArr =[]

while(gradesCount >= 1):
    grade = float(input("Please add your grade: "))
    gradesArr.append(grade)
    gradesCount = gradesCount - 1


while(gradesCount < numberOfGrades):
    print(gradesArr[gradesCount]"%")
    gradesCount = gradesCount + 1



