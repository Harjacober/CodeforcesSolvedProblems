n = int(input())
num = list(map(int, input().split()))
a = num.index(n)
b = num.index(1)
ans = [b-a]
if b > a:
    ans.append(n-a-1)
    ans.append(b-0)
elif a > b:
    ans.append(n-b-1)
    ans.append(a-0)
print(max(ans))    
    
