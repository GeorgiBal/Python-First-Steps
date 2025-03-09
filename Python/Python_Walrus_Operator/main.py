# foods = list()
# while True:
#     food = input("What food do you like: ")
#     if food.lower() == "quit":
#         break
#     foods.append(food)

foods = list()
while (food := input("What food do you like: ")) != "quit":
    foods.append(food)
print(foods)
