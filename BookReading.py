def bookReading(n, m):
    summ = 0
    if m*10 < n: 
        for i in range(m, m*10+1, m): 
            summ += i%10
        summ = summ*(n//(m*10))        
        rem = n%(m*10)
        for i in range(m, rem+1, m):
                summ += i%10
    else:
        for i in range(m, n+1, m):
                summ += i%10
    return summ

t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    print(bookReading(arr[0], arr[1])) 
