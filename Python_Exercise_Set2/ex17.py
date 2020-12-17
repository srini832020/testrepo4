try:
    fo=open("new.txt","r")
    fo.write("just writing in read mode")
except IOError:
    print"Failed to write/read data"
else:
    print"written successfully"
