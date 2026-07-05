M = int(input("enter # of movements taken by the snail: "))
p = [(0, 0)]
x = p[0][0]
y = p[0][1]
for i in range(M):
    a = input("Enter movement: ")
    d = a[0]
    n = int(a[1:])
    if d == "N":
        for j in range(n):
            x = x
            y += 1
            p.append((x, y))
    if d == "E":
        for j in range(n):
            x += 1
            y = y
            p.append((x, y))
    if d == "S":
        for j in range(n):
            x = x
            y -= 1
            p.append((x, y))
    if d == "W":
        for j in range(n):
            x -= 1
            y = y
            p.append((x, y))
print(len(p)-len(set(p)))
