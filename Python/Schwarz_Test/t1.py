beer = 200
wine = 300
beer_orders = 0
beer_deliveries = 0
wine_orders = 0
wine_deliveries = 0

while True:
    line = input().split()
    if line[0] == "END":
        break
    if line[0] == "Beers:":
        if int(line[1]) < 0:
            beer_orders += 1
            beer += int(line[1])
        else:
            beer_deliveries += 1
            beer += int(line[1])
    elif line[0] == "Wines:":
        if int(line[1]) < 0:
            wine_orders += 1
            wine += int(line[1])
        else:
            wine_deliveries += 1
            wine += int(line[1])

print(f"Wine: {wine}\nDeliveries: {wine_deliveries}\nOrders: {wine_orders}")
print(f"Beer: {beer}\nDeliveries: {beer_deliveries}\nOrders: {beer_orders}")
