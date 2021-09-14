src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []

for i in src:
    if src.count(i) == 1:
        result.append(i)

print(result)

print('_' * 70)

unique_num = []
tmp = []

for i in src:
    if i not in tmp:
        unique_num.append(i)
    elif unique_num != [] and i in unique_num:
        unique_num.remove(i)
    tmp.append(i)

print(unique_num)