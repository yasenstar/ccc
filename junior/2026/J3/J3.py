Ngoc = input("All in capital, for Ngoc's candies: ")
Minh = input("All in capitcal, for Minh's candies: ")

n = []
m = []

for i in Ngoc:
    n.append(i)

for i in Minh:
    m.append(i)

print(len(n), len(m))

compete_num = min(len(n), len(m))

score_n = 0
score_m = 0

for i in range(compete_num):
    if n[i] == m[i]:
        score_n = score_n + 1
        score_m = score_m + 1
        n.pop(i)
        m.pop(i)
        compete_num = min(len(n), len(m))
        print(compete_num)

print(Ngoc, score_n)

print(Minh, score_m)