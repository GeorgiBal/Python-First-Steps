items = ['apple', 'banana', 'orange']
count = [3, 6, 4]
price = [1.20, 1.50, 1.80]

for (items, count, price) in zip(items, count, price):
    sentence = 'I bought ' + str(count) + ' ' + str(items) + 's at price ' + str(price) + ' dollars.'
    print(sentence)
