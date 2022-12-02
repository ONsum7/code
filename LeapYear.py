#W3T1
print('is it a leap year program')

year = int(input('Enter a year '))
print('')

if (year % 400 == 0) and (year % 100 == 0):
    print(year, 'is a leap year')
elif (year % 4 ==0) and (year % 100 != 0):
    print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')