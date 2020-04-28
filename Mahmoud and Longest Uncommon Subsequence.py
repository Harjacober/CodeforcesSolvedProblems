a,b = input(),input()
if len(a)>len(b):
    longest, shortest = a,b
else:
    longest, shortest = b,a
if longest != shortest:
    print(len(longest))
else:
    print(-1)
    
