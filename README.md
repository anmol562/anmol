# anmol
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    else:
        return result
    finally:
        print("Division attempt finished.")
