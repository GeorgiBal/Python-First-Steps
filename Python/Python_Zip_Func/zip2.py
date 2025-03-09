username = ["Miro", "Tom", "Bob"]
password = ("miro123", "tom123", "bob123")

users = dict(zip(username, password))
for key, value in users.items():
    print(f"{key} - {value}")
