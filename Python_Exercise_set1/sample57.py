try:
    var=10
    if var > 5:
        raise ZeroDivisionError("My own error")
except ZeroDivisionError as v:
    print(v)
         
