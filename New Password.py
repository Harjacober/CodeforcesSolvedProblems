n,k = list(map(int, input().split()))
arr = []
for i in range(k):
    arr.append(chr(97+i))
for j in range(n-k): 
    arr.append(arr[j])
print(''.join(arr))
