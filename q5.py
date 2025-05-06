# 5. Make value errors handler with built in exceptions
try:
    num = int('abc')
except ValueError:
    print("Invalid value for integer conversion")
