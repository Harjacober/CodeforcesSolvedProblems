def pair(a,b):
    diff = []
    for i in range(len(a)):
        diff.append(a[i]-b[i])

    count = 0 
    for j in range(len(diff)):
        k = j+1
        while k < len(diff):
            if diff[k]+diff[j]>0:
                count += 1
            k += 1
    return count

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(pair(a,b)) 
