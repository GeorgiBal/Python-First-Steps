import re

text = 'random string. MyName123@gmail.com . more random string YourName123@gmail.com'
pattern = re.compile("[a-zA-Z0-9]+@+[a-zA-Z0-9]+\.[a-zA-Z0-9]+")
result = pattern.findall(text)
print(result)
