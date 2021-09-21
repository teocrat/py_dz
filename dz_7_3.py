import os
import shutil

dir_path = 'my_project'
dir_name = 'templates'
try:
    for root, dirs, files in os.walk(dir_path):
        if dir_name in dirs and root != dir_path:
            for i in os.listdir(os.path.join(root, dir_name)):
                shutil.copytree(os.path.join(root, dir_name, i), os.path.join(dir_path, dir_name, i))
except FileExistsError:
    print('Такая папка уже существует')
