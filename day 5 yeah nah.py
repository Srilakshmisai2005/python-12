x,y=input().split()
x,y=int(x),int(y)
list_a=[]
if(x>0) and (y>0):
    for i in range(1,x+1):
        if(x%i==0):
            list_a.append(i)
    for i in range(1,y+1):
        if(y%i==0):
            list_a.append(i)
    b=set()
    for i in list_a:
        if(list_a.count(i)==2):
           b.add(i)
    c=sum(list(b))
    d=(x*y)%c
    if(d==0):
        print("YEAH")
    else:
        print("NAH")
else:print("NAH")
