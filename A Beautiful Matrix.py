for row in range(5):
    r = input().split()
    for col in range(len(r)):
        if r[col] == '1':
            cord = (row, col)
            break

rowdiff = abs(2-cord[0])+ abs(2-cord[1])
print(rowdiff)

            
