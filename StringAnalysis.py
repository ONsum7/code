#W3T3
String = input('Enter some text ')
vow = 0
Digits = 0
Conc = 0
Spaces = 0
Punc = 0

String = String.lower()

for i in range(0, len(String)):
    if(String[i] == 'a'or String[i] == 'e' or String[i] == 'i'
    or String[i] == 'o' or String[i] == 'u'):
        vow = vow + 1
    
    elif((String[i] >= 'a'and String[i] <= 'z')):
        Conc = Conc + 1
    
    elif( String[i] >= '0' and String[i] <= '9'):
        Digits = Digits + 1
    
    elif (String[i] ==' ' or String[i] == '\t'):
        Spaces = Spaces + 1
        
    else:
        Punc = Punc + 1
    
print('')
print('analysis of text')
print('-' *16)

print('Number of vow = ', vow)
print('Number of Conc = ', Conc)
print('Number of Digits = ', Digits)
print('Number of Spaces = ', Spaces)
print('Number of Punc = ', Punc)