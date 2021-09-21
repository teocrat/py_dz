import os

from collections import defaultdict

dir_path = 'some_data'
result = defaultdict(int)

for root, dirs, files in os.walk(dir_path):
    for file in files:
        size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
        result[size] += 1

for size, nums in sorted(result.items()):
    print(f'{size}: {nums}')
