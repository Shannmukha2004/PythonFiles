def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error"
print(divide(6,3))