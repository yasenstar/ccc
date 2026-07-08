n = int(input("Number of parking spots: "))
l = int(input("Number of lights: "))
q = int(input("Number of parking spots you will be questioned about: "))

print(n,l,q)

p=[]
s=[]

for i in range(l):
    num1, num2 = map(int, input("Enter number of parking spot above and spread, separate by space: ").split())
    p.append(num1)
    s.append(num2)

print(p)
print(s)

illum_list = ["N"]*n
print(illum_list)

for i in range(len(p)):
    if p[i]-1-s[i] <= 0:
        for j in range(0,p[i]-1+s[i]):
            illum_list[j] = "Y"
    elif p[i]-1-s[i] >= n-1:
        for j in range(p[i]-1-s[i],n-1):
            illum_list[j] = "Y"
    else:
        for j in range(p[i]-1-s[i],p[i]-1+s[i]):
            illum_list[j] = "Y"

num_q = []
for i in range(q):
    num_q.append(int(input("questioned spot: ")))

for i in num_q:
    print(illum_list[i-1])