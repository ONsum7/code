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

with open('studentmark.txt', 'r') as f:
  marks = f.readlines()

marks = [int(mark) for mark in marks]

average_mark = sum(marks) / len(marks)

max_mark = max(marks)
min_mark = min(marks)

with open('studentmark.txt', 'a') as f:
  f.write(f'\nAverage mark: {average_mark}\n')

  f.write(f'Max mark: {max_mark}\n')
  f.write(f'Min mark: {min_mark}\n')

  for mark in marks:
    if mark >= 40:
      f.write(f'Mark {mark} is a pass\n')
    else:
      f.write(f'Mark {mark} is a fail\n')


f.close()