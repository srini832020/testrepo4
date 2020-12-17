fo=open("new.txt","r+")
print"name of the file:",fo.name
str=fo.read()
print"File reading is completed:",str
fo.close()
