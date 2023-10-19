import os
import subprocess
import sys

def git_current_path():
    subprocess.run(['pwd', 'cd/..'])
git_current_path()


def get_user_path():
    if len(sys.argv) < 2:
        print("Please provide a path argument.")
        return None
    else:
        user_path = sys.argv[1]
        return user_path

path = get_user_path()
if path:
    # dir_path = '/home/falah/Documents/my-github/';
    def git_pull_all(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                git_dir = os.path.join(item_path, '.git')
                if os.path.exists(git_dir):
                    print(f'Pulling repository: {item_path}')
                    subprocess.run(['git', '-C', item_path, 'pull'])
                    print('Pull complete.\n')
            else :
                    print("Pull Faild")

    git_pull_all(path)
else:
    path = git_current_path()

# Specify the directory path where you want to perform git pull

# directory_path = '.'
# if path:
#     git_pull_all(path)
# else:
#     git_pull_all(directory_path)
