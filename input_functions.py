#input_functions
valid = False
while valid == False:
    numstr = input('please enter a number between 0 and 100 ')
    if (numstr.isnumeric()):
        num = int(numstr)
        print('')
        print('your number is',num)
        valid = True
    else:
        print('This is not an integer')

valid = False
print('')

def isfloat(numstr):
        try:
            float(numstr)
            return True
        except ValueError:
            return False

while valid == False:
    flostr = input('please enter a float number between 0 and 100 ' )
    if (numstr.isnumeric()):
        numfl = float(flostr)
        if isfloat(numstr) == True:
            print('')
            print('your number is', numfl)
            valid = True
        else:
            print('not a float')
    else:
        print('not a float')