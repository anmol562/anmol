# 3. Make a key error handler with built in exceptions
try:
    d = {'a': 1}
    print(d['b'])
except KeyError:
    print("Key not found in dictionary")

