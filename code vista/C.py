n, c = [int(i) for i in input().split(" ")]

conflict_pairs = []
for _ in range(c):
    a, b = [int(i) for i in input().split(" ")]
    conflict_pairs.append((a, b))

exp = [int(i) for i in input().split(" ")]

conflict_map = {}
for i in range(1, n + 1):
    conflict_map[i] = []

for a, b in conflict_pairs:
    conflict_map[a].append(b)
    conflict_map[b].append(a)

max_total = 0

for i in range(1, n + 1):
    team = [i]
    total = exp[i - 1]
    
    for j in range(1, n + 1): 
        if j in team:
            continue
        can_add = True
        for member in team:
            if j in conflict_map[member]:
                can_add = False
                break
        if can_add:
            team.append(j)
            total += exp[j - 1]
    
    if total > max_total:
        max_total = total

print(max_total)
