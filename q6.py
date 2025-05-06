# 6. Make attribute errors handler with built in exceptions
try:
    x = 10
    x.append(5)
except AttributeError:
    print("Attribute not found for the object")


