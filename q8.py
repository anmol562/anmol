# 8. Make module not found error handler with built in exceptions
try:
    import nonexistentmodule
except ModuleNotFoundError:
    print("Module not found")
