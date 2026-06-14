Ngoc = input("All in capital, for Ngoc's candies: ")
Minh = input("All in capitcal, for Minh's candies: ")

print(len(Ngoc), len(Minh))

compete_num = min(len(Ngoc), len(Minh))

score_n = 0
score_m = 0

for i in range(compete_num):
    if Ngoc[i] == Minh[i]:
        score_n = score_n + 1
        score_m = score_m + 1
        Ngoc.pop(i)
        Minh.pop(i)

print(Ngoc, score_n)

print(Minh, score_m)