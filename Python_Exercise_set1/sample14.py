count=0
def Fun():
    global count
    print("My function",count)
    count+=1
    if count==20:
        return
    else:
        Fun()
Fun()

def Fun(**score):
    print(score)
Fun(score=30,name='dhoni')
    
     



