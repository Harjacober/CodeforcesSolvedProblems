def jumps(path):
    ans,count = 0,1
    for e in path[::-1]:
        if e!= 'R':
            count += 1
        else: count = 1
        ans = max(ans, count)
    return ans

t = int(input())
for _ in range(t):
    string = input()
    print(jumps(string))
