print('Enter your name, your age, where you live, eye colour: ')
ID = input()

name = ID[:ID.index(',')]

age = ID[ID.index(',') + 1:]
age_ID = age[:age.index(',')]

town = age[age.index(',') + 1:]
town_ID = town[:town.index(',')]

eye_colour = ID[ID.rindex(',') + 2:]
print('Name - ' + name)
print('Age - ' + age_ID)
print('Town - ' + town_ID)
print('Eye colour - ' + eye_colour)
