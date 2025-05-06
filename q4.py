# 4. Make index error handler with built in exceptions
try:
    l = [1, 2, 3]
    print(l[5])
except IndexError:
    print("Index out of range")
