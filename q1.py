# 1. Make a zero division error handler with built in exceptions
try:
    a = 10
    b = 0
    c = a / b
except ZeroDivisionError:
    print("Cannot divide by zero")
