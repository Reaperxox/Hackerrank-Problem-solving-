l=[]
l1=[]
l2=[]
n=int(input())
for k in range(n):
 ar=input().split(" ")
 ar=[int(i) for i in ar]
 ar=ar[0:n]
 l.append(ar)



for i in range(n):
    l1.append(l[i][i])
l=l[::-1]
for j in range(n):
    l2.append(l[j][j])



   
print(abs(sum(l1)-sum(l2)))  


