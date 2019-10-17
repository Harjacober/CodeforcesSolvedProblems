def wrongSubtraction(n, k):
    for i in range(k):
        if n%10 == 0:
            n = n//10
        else:
            n = n-1
    return n

lis = list(map(int, input().split()))
print(wrongSubtraction(lis[0] , lis[1]))
