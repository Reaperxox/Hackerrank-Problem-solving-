l1=input().split(" ")
l1=[int(i) for i in l1]
l1=l1[0:3]
l2=input().split(" ")
l2=[int(i) for i in l2]
l2=l2[0:3]
sc1=0
sc2=0

a=list(zip(l1,l2))

for i in range(len(l1)):
    if a[i][0]>a[i][1]:
        sc1+=1
    if a[i][0]<a[i][1]:
        sc2+=1
    if a[i][0]==a[i][1]:
        sc1+=0
        
      
print(sc1,sc2)
        
        