for i in range(int(input())):
    s = input()
    if len(s) <= 10:
        print(s)
    else:
        print("{}{}{}".format(s[0],len(s)-2,s[-1]))
