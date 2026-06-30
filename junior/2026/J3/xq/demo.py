# n = input("Ngoc candy: ")
n = "RGBBGBBG"
m = "GBGRR"
print(n)
print(len(n))
# print(n[0])

# for i in n:
#     print(i)

# for j in m:
#     print(j)

print(n[0], m[0])

score_n = 0
score_m = 0

print(score_n, score_m)

if n[0] == 'R':
    if m[0] == "G":
        print("n is win")
        score_n = score_n + 1
    elif m[0] == "B":
        print("m is win")
    else:
        print("both are red")

print(score_n, score_m)
# def compare():