src = [300, 2, 12, 44, 2, 2, 5, 30, 3, 45, 88, 6, 7, 69, 45]
i = 1
result = []

while i != len(src):
    if src[i - 1] < src[i]:
        result.append(src[i])
    i += 1

print(result)
