n=int(input())
l1=[]
l2=[]
for i in range(n):
    m=int(input())
    l1.append(m)

for j in l1:
    
    if j>=38:
    
        if (j+2)%5==0:
            l2.append(j+2)
        elif(j+1)%5==0:
            l2.append(j+1)
        else:
            l2.append(j)
    else:
        l2.append(j)
        
        
for k in l2:
    print(k)
        