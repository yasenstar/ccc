def candy(a, b):
    x = 0
    y = 0
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] == "R" and b[j] == "G":
            j += 1
            x += 1
        elif a[i] == "G" and b[j] == "R":
            i += 1
            y += 1
        elif a[i] == "G" and b[j] == "B":
            j += 1
            x += 1
        elif a[i] == "B" and b[j] == "G":
            i += 1
            y += 1
        elif a[i] == "B" and b[j] == "R":
            j += 1
            x += 1
        elif a[i] == "R" and b[j] == "B":
            i += 1
            y += 1
        elif a[i] == 'R' and b[j] == "R":
            i += 1
            j += 1
            x += 1
            y += 1
        elif a[i] == 'G' and b[j] == "G":
            i += 1
            j += 1
            x += 1
            y += 1
        elif a[i] == 'B' and b[j] == "B":
            i += 1
            j += 1
            x += 1
            y += 1
    if i == len(a) or j == len(b):
        if i == len(a):
            y += len(b) - j
        if j == len(b):
            x += len(a) - i
    return str(x) + '\n' + str(y)

n = input("Enter Ngoc candy: ")
m = input("Enter Minh candy: ")
result = candy(n, m)
print(result)