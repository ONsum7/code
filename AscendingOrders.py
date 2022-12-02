#W2T3
print('Ascending order')
print('')
FStr = input('Input the first number ')
SStr = input('input the second number ')
print('')

FNum = int(FStr)
SNum = int(SStr)
 
if FNum > SNum:
    print('your number has been swapped ')
    print('First number is ', SNum)
    print('Second number is ', FNum)
else:
    print('First number is ', FNum)
    print('Second number is ', SNum)
    print('your number has not been swapped ')