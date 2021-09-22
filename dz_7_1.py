import os

dir_path = {'my_project_1': [{'settings': []}, {'mainapp': []}, {'adminapp': []}, {'authapp': []}]}

for k, v in dir_path.items():
    if not os.path.exists(k):
        for item in v:
            for n in item.keys():
                os.makedirs(os.path.join(k, n))
