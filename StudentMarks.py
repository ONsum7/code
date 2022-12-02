StuList = []
  
NumOfStudents = int(input("Enter number of student marks "))
  
for i in range(0, NumOfStudents):
    Mark = int(input('Please enter mark '))
  
    StuList.append(Mark) 
    

Average = sum(StuList) / len(StuList)
AverageR= round(Average,2)
AverageStr = str(AverageR)
print(' ')

print('your Average mark is ' + AverageStr)
print('minimum mark is', min(StuList))
print('maximum mark is', max(StuList))

StuList.sort()

print(' ')

print("Student No.\tMark\t Result")
StudentNo = 1


for i in range(0, len(StuList)):
    if StuList[StudentNo-1] >= 40:
        print( StudentNo , '\t\t' , StuList[StudentNo-1] , '\tPass')
    else:
        print( StudentNo , '\t\t' , StuList[StudentNo-1] , '\tfail')
    StudentNo = StudentNo + 1
