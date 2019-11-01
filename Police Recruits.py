n = int(input())
query = input().split()
recruits = 0
unsolved = 0
for e in query:
    if e == "-1":
        if recruits > 0:
            recruits -= 1
        else:
            unsolved += 1
    else:
        recruits += int(e)

print(unsolved)        
