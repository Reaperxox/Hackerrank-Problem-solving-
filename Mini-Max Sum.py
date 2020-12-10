arr = list(map(int, input().rstrip().split()))
arr=arr[0:5]
arr1=[i for i in arr]



arr.remove(min(arr))


arr1.remove(max(arr1))
print(sum(arr1),sum(arr))
    
    
