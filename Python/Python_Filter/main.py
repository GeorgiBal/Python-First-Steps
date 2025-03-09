friends = [("Ivan", 12),
           ("Bob", 20),
           ("Kiro", 18),
           ("Miro", 15),
           ("Nico", 19)]

age = lambda data: data[1] >= 18
drinking_buddies = list(filter(age, friends))
print(drinking_buddies)
