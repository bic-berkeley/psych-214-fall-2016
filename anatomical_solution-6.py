#- Find candidates for I
candidates = []
for i in range(120, 201):
    if P % i == 0:
        candidates.append(i)
candidates
# [120, 130, 136, 156, 170, 195]
