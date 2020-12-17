try:
    print('dhoni'+7)
except (ZeroDivisionError,TypeError) as a:
    print(a)
else:
    print("else here")
finally:
    print("Finally here")
    

