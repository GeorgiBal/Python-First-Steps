# import project2

print(__name__)
# print(project2.__name__)

if __name__ == "__main__":
    print("Running this module directly")
else:
    print("Running other module indirectly")


def hello():
    print("Hellooooo")


if __name__ == "__main__":
    hello()
