import requests


def convert(amount):
    response = requests.get('https://api.exchangerate-api.com/v4/latest/GBP')
    print(response.json())
    exchange_rates = response.json()['rates']
    usd_rate = exchange_rates['USD']
    usd_amount = usd_rate*amount

    return usd_amount


pounds = int(input("Enter an amount of pounds: "))
us_dollars = convert(pounds)
print(f"{pounds:.2f} = {us_dollars:.2f}")
