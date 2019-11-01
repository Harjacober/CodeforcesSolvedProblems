u,l = 0,0
string = input()
for s in string:
    if s.isupper():
        u += 1
    else:
        l += 1

if u > l:
    print(string.upper())
else:
    print(string.lower())
