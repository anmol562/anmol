# 7. Make file not found error handler with built in exceptions
try:
    f = open('nofile.txt')
except FileNotFoundError:
    print("File not found")
