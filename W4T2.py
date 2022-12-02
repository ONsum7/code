#W4T2
print('Star Wars name generator'.center(40))
print('')

FName = str(input('please enter your first name '))
LName = str(input('please enter your last name '))
MaidenName = str(input('please enter your mother maiden name '))
City = str(input('please enter the name of the city you were born in '))
print('')

FNameL = FName.lower()
LNameL = LName.lower()
MaidenNameL = MaidenName.lower()
CityL = City.lower()

StarFirst = FNameL[:3] + LNameL[:2]
StarLast = MaidenNameL[:2] + CityL [:3]
        
StarWarsName = StarFirst.capitalize() +' '+ StarLast.capitalize()
print('Your Star Wars name is ' + StarWarsName)