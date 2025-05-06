# 9. Make an error handler with the use of multiple except for all types of errors
try:
    a = 10 / 0
    b = int('abc')
    c = d['key']
except ZeroDivisionError:
    print("Zero Division Error")
except ValueError:
    print("Value Error")
except KeyError:
    print("Key Error")
except Exception as e:
    print("Other Error:", e)
