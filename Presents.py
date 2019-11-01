n = int(input())
friends = list(map(int, input().split()))
arr = [0]*n
for i in range(n):
    arr[friends[i]-1] = i+1  
print(*arr, sep=" ")
