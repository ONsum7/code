

StudentDatabase = { 
    "ID": ['10101010','01010101','01110111','01001110'],
      "FirstName": ['Amy','Alexander','Jason','Seren'],
      "LastName": ['Harrison','Moore','Marshall','Hussain'],
      "Course": ['BIT','Computer Science','CIT','BIT'],
      "Year": ['1','1','2','2']
  }

digit = input('enter the student ID ')

check = 0
if digit == '10101010':
    Num = 0
    print('Student ID' ,digit, 'is in the database')
    print('')
    print('First name:','\t', StudentDatabase['FirstName'][Num])
    print('Last name:','\t', StudentDatabase['LastName'][Num])
    print('Course name:','\t', StudentDatabase['Course'][Num])
    print('Year:','\t\t', StudentDatabase['Year'][Num])
    check = 1
    
elif digit == '01010101':
    Num = 1
    print('Student ID' ,digit, 'is in the database')
    print('')
    print('First name:','\t', StudentDatabase['FirstName'][Num])
    print('Last name:','\t', StudentDatabase['LastName'][Num])
    print('Course name:','\t', StudentDatabase['Course'][Num])
    print('Year:','\t\t', StudentDatabase['Year'][Num])
    check = 1
    
elif digit == '01110111':
    Num = 2
    print('Student ID' ,digit, 'is in the database')
    print('')
    print('First name:','\t', StudentDatabase['FirstName'][Num])
    print('Last name:','\t', StudentDatabase['LastName'][Num])
    print('Course name:','\t', StudentDatabase['Course'][Num])
    print('Year:','\t\t', StudentDatabase['Year'][Num])
    check = 1
    
elif digit == '01001110':
    Num = 3
    print('Student ID' ,digit, 'is in the database')
    print('')
    print('First name:','\t', StudentDatabase['FirstName'][Num])
    print('Last name:','\t', StudentDatabase['LastName'][Num])
    print('Course name:','\t', StudentDatabase['Course'][Num])
    print('Year:','\t\t', StudentDatabase['Year'][Num])
    check = 1
    
else:
    print('student ID', digit,'not recognised')
   

print('')


StudentDataB = {'10101010': 'Amy \t\t Harrison \t BIT \t\t\t 1',
         '01010101': 'Alexander \t Moore \t\t Computer Science    \t1',
         '01110111': 'Jason \t\t Marshall \t CIT \t\t\t 2',
         '01001110': 'Seren \t\t Harrison \t BIT \t\t\t 2'}

print('')
print('Student List:')
print('')
print('ID','\t\t','First Name','\t','Last Name','\t','Course Name','\t\t','Year')
if check == 1:
    for i in StudentDataB:
        print(i + '\t', (StudentDataB)[i])