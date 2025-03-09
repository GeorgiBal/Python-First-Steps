beer = 200
wine = 300
beer_orders = 0
wine_orders = 0
beer_deliveries = 0
wine_deliveries = 0

while True:
    text = input()
    if text == 'END':
        break
    else:
        text = text.split(': ')
        num = int(text[1])

    if text[0] == 'Wines':
        if num > 0:
            wine += num
            wine_deliveries += 1
        else:
            wine += num
            wine_orders += 1
    elif text[0] == 'Beers':
        if num > 0:
            beer += num
            beer_deliveries += 1
        else:
            beer += num
            beer_orders += 1


print('Wines: ' + str(wine))
print('Deliveries: ' + str(wine_deliveries))
print('Orders: ' + str(wine_orders))
print('Beer: ' + str(beer))
print('Deliveries: ' + str(beer_deliveries))
print('Orders: ' + str(beer_orders))
