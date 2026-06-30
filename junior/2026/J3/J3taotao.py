n = input("Enter Ngoc candy: ")
m = input("Enter Minh candy: ")
def candy(a, b):
    x = 0
    y = 0
    if len(a) == "0" or len(b) == "0":
        if len(a) == "0":
            x += len(b)
            return
        elif len(b) == "0":
            y += len(a)
            return
    elif a[0] == "R" and b[0] == "G":
        x += 1
    elif a[0] == "G" and b[0] == "R":
        y += 1
    elif a[0] == "G" and b[0] == "B":
        x += 1
    elif a[0] == "B" and b[0] == "G":
        y += 1
    elif a[0] == "B" and b[0] == "R":
        x += 1
    elif a[0] == "R" and b[0] == "B":
        y += 1
    elif a[0] == 'R' and b[0] == "R":
        x += 1
        y += 1
    elif a[0] == 'G' and b[0] == "G":
        x += 1
        y += 1   
    elif a[0] == 'B' and b[0] == "B":
        x += 1
        y += 1
    return (x, y)
while len(n) > 0 and len(m) > 0:
    result = candy(n, m)
    print(result)