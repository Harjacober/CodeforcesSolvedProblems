def indexOfStudents(n, arr):
    arrs = ''.join(arr)
    double = ''.join([str(i%n+1) for i in range(n*2)])
    
    reverse = double[::-1]
    print(double, reverse)
    if (arrs in double) or (arrs in reverse):
        return "YES"
    else:
        return "NO"
k = int(input())
for i in range(k):
    n = int(input())
    arr = list(map(str, input().split()))
    print(indexOfStudents(n, arr))
