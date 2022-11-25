#W4T1
Name = str(input('Please enter your name> '))

NameUp = Name.upper()
print(NameUp)

NameSplit = Name.split(" ")[0].capitalize() + ' ' + Name.split(" ")[1].capitalize()
print(NameSplit)

NameLow = Name.lower()
print(NameLow)

print('~' * 48)
print('~' + ' '.center(46) + '~')
print('~' + NameUp.ljust(46) + '~')
print('~' + ' '.center(46) + '~')
print('~' + NameSplit.center(46) + '~')
print('~' + ' '.center(46) + '~')
print('~' + NameLow.rjust(46) + '~')
print('~' * 48)
