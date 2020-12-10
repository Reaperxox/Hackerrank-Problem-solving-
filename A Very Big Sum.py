n=int(input())
for k in range(n):
 ar=input().split(" ")
 ar=[int(i) for i in ar]
 ar=ar[0:n]


print(sum(ar))