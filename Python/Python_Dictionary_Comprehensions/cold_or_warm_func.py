cities = {"New York": 32,
          "Boston": 75,
          "Los Angeles": 100,
          "Chicago": 50}


def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 70 > value >= 40:
        return "WARM"
    else:
        return "COLD"


desc_cities = {key: check_temp(value) for (key, value) in cities.items()}
print(desc_cities)
