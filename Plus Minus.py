n=int(input())
arr = list(map(int, input().rstrip().split()))
arr=arr[0:n]
cn=0
cp=0
cz=0
for i in arr:
 if i > 0:
   cp+=1
 elif i == 0:
   cz+=1
 else:
   cn+=1
   
print ('%.6f'%(cp/n))
print ('%.6f'%(cn/n))
print ('%.6f'%(cz/n))