n=int(input())
arr = list(map(int, input().rstrip().split()))
arr=arr[0:n]

m=max(arr)
print(arr.count(m))