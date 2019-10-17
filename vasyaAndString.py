def vasya(n, kere, string):
    k = kere
    #string = [a for a in stri] 
    count = 1
    ans = count
    for i in range(n-1):
        for j in range(i+1, n): 
            if string[i] == string[j] :
                count += 1
            else:
                if k > 0:
                    count += 1
                    k -= 1 
                else:
                    break 
        if count > ans:
            ans = count
        count = 1
        k = kere
    return ans

lis = list(map(int, input().split()))
string = input()
print(vasya(lis[0], lis[1], string))
