StuList = []
  
NumOfStudents = int(input("Enter number of student marks "))
  
for i in range(0, NumOfStudents):
    ele = int(input('Please enter mark '))
  
    StuList.append(ele) 
    
average = sum(StuList) / len(StuList)
averageR= round(average,2)
averagestr = str(averageR)
print(' ')

print('your average mark is ' + averagestr)
print('minimum mark is', min(StuList))
print('maximum mark is', max(StuList))

StuList.sort()
print(StuList)

print(' ')

print("Student No.\tMark\t Result")
StudentNo = 1


for i in range(0, len(StuList)):
    if StuList[StudentNo-1] >= 40:
     print( StudentNo , '\t\t' , StuList[StudentNo-1] , '\tPass')
    else:
     print( StudentNo , '\t\t' , StuList[StudentNo-1] , '\tfail')
    StudentNo = StudentNo + 1
