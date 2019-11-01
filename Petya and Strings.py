first = input().lower()
second = input().lower()
if first < second:
    print(-1)
elif second < first:
    print(1)
else:
    print(0)
