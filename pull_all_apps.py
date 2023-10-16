import os
import subprocess

dir_path = '/home/falah/Documents/my-github/';
def git_pull_all(dir_path):
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            git_dir = os.path.join(item_path, '.git')
            if os.path.exists(git_dir):
                print(f'Pulling repository: {item_path}')
                subprocess.run(['git', '-C', item_path, 'pull'])
                print('Pull complete.\n')
    else :
                print("Pull Faild")
# Specify the directory path where you want to perform git pull
directory_path = '/home/falah/Documents/my-github/'

git_pull_all(directory_path)
