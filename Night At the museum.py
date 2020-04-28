s = input()
ans = 0
prev = ord('a')
for i in range(len(s)):
    curr = ord(s[i]) 
    ans += min((prev-curr)%26, (curr-prev)%26)
    prev = curr

print(ans)
