n = input("Enter Ngoc candy: ")
m = input("Enter Minh candy: ")
def candy(a, b):
    x = 0
    y = 0
    if len(a) == "0" or len(b) == "0":
        if len(a) == "0":
            x += len(b)
            return (x, y)
        elif len(b) == "0":
            y += len(a)
            return
    elif a[0] == "R" and b[0] == "G":
        b[1:]
        x += 1
    elif a[0] == "G" and b[0] == "R":
        a[1:]
        y += 1
    elif a[0] == "G" and b[0] == "B":
        b[1:]
        x += 1
    elif a[0] == "B" and b[0] == "G":
        a[1:]
        y += 1
    elif a[0] == "B" and b[0] == "R":
        b[1:]
        x += 1
    elif a[0] == "R" and b[0] == "B":
        a[1:]
        y += 1
    elif a[0] == 'R' and b[0] == "R":
        a[1:]
        b[1:]
        d += 1
        x += 1
        y += 1
    elif a[0] == 'G' and b[0] == "G":
        a[1:]
        b[1:]
        x += 1
        y += 1   
    elif a[0] == 'B' and b[0] == "B":
        a[1:]
        b[1:]
        x += 1
        y += 1
result = candy(n, m)
print(result)