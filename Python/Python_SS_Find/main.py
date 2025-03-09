team = 'GK, CB, CM, ST'

GK = team[:team.find(',')]

CB_position = team[team.find(',') + 2:]
CB = CB_position[:CB_position.find(',')]

CM_position = CB_position[CB_position.find(',') + 2:]
CM = CM_position[:CM_position.find(',')]

ST = team[team.rfind(',') + 2:]

print(GK)
print(CB)
print(CM)
print(ST)
