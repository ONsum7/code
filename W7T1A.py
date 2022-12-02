f = open('studentmark.txt', 'wt')
Marks = (input('enter a number of student marks to store '))
counter = 0
MarksInt = int(Marks)

while counter != MarksInt:
    StudentMark = (input('Enter a mark '))
    f.write(StudentMark)
    f.write('\n')
    counter = counter + 1
    
print('')
print('Marks have been saved')
print('')

f.close()