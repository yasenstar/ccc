S = []
for i in range(1,6):
    S.append(int(input(f"Raw score for #{i} judge: ")))
D = int(input("Difficulty factor: "))

max_score = max(S)
max_index = S.index(max_score)

S.pop(max_index)

min_score = min(S)
min_index = S.index(min_score)

S.pop(min_index)

print(sum(S)*D)