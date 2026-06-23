def compare(i, j, ni, mj, sn, sm):
    if (ni == 'R'):
        if (mj == 'G'):
            print("Ngoc[",i,"] wins")
            sn = sn + 1
            j = j + 1
        elif (mj == 'B'):
            print("Minh[",j,"] wins")
            sm = sm + 1
            i = i + 1
        else:
            print("Both are Red in same color")
            sn = sn + 1
            sm = sm + 1
            i = i + 1
            j = j + 1
    elif (ni == 'G'):
        if (mj == 'B'):
            print("Ngoc[",i,"] wins")
            sn = sn + 1
            j = j + 1
        elif (mj == 'R'):
            print("Minh[",j,"] wins")
            sm = sm + 1
            i = i + 1
        else:
            print("Both are Green in same color")
            sn = sn + 1
            sm = sm + 1
            i = i + 1
            j = j + 1
    else:
        if (mj == 'R'):
            print("Ngoc[",i,"] wins")
            sn = sn + 1
            j = j + 1
        elif (mj == 'G'):
            print("Minh[",j,"] wins")
            sm = sm + 1
            i + i + 1
        else:
            print("Both are Blue in same color")
            sm = sm + 1
            i = i + 1
            j = j + 1
    return i, j, sn, sm


Ngoc = input("All in capital, for Ngoc's candies: ")
Minh = input("All in capitcal, for Minh's candies: ")

n = []
m = []

for i in Ngoc:
    n.append(i)

for i in Minh:
    m.append(i)

print(len(n), len(m))

print(n, m)

print(min(len(n),len(m)))

smaller = min(len(n),len(m))

i = 0

j = 0

sn = 0

sm = 0

while (i<=(smaller-1)):
    j = i
    i, j, sn, sm = compare(i,j,n[i],m[j],sn,sm)

print("sn = ", sn)
print("sm = ", sm)