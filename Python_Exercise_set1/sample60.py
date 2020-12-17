class yeserror(Exception):
    #pass
    var="user created error"
try:
    var=10
    if var > 5:
        raise yeserror
except yeserror as v:
    print(v.var)
         
