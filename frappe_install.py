import subprocess
import requests

subprocess.check_call(['sudo', 'apt-get', 'update','-y'])
subprocess.check_call(['sudo', 'apt-get', 'upgrade','-y'])

def Install_GIT_shell_commands(commands):
    for command in commands:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Check the return code to see if the command executed successfully
        if result.returncode == 0:
            # Print the output of the command
            print(result.stdout)
        else:
            # Print the error message
            print(result.stderr)


commands_to_execute = [
    "sudo apt-get install git"
]
Install_GIT_shell_commands(commands_to_execute)


def Install_Python_shell_commands(commands):
    for command in commands:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Check the return code to see if the command executed successfully
        if result.returncode == 0:
            # Print the output of the command
            print(result.stdout)
        else:
            # Print the error message
            print(result.stderr)


commands_to_execute = [
    "sudo apt-get install python3-dev python3.10-dev python3-setuptools python3-pip python3-distutils"
]
Install_Python_shell_commands(commands_to_execute)

def Install_Python_Virtual_Env_shell_commands(commands):
    for command in commands:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Check the return code to see if the command executed successfully
        if result.returncode == 0:
            # Print the output of the command
            print(result.stdout)
        else:
            # Print the error message
            print(result.stderr)


commands_to_execute = [
    "sudo apt-get install python3-dev python3.10-dev python3-setuptools python3-pip python3-distutils"
]
Install_Python_Virtual_Env_shell_commands(commands_to_execute)

def Install_Python_Virtual_Env_shell_commands(commands):
    for command in commands:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Check the return code to see if the command executed successfully
        if result.returncode == 0:
            # Print the output of the command
            print(result.stdout)
        else:
            # Print the error message
            print(result.stderr)


commands_to_execute = [
    "sudo apt-get install python3.10-venv"
]
Install_Python_Virtual_Env_shell_commands(commands_to_execute)

def Install_software_properties_shell_commands(commands):
    for command in commands:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Check the return code to see if the command executed successfully
        if result.returncode == 0:
            # Print the output of the command
            print(result.stdout)
        else:
            # Print the error message
            print(result.stderr)


commands_to_execute = [
    "sudo apt-get install software-properties-common"
]
Install_software_properties_shell_commands(commands_to_execute)

def Install_mariadb_shell_commands(commands):
    for command in commands:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Check the return code to see if the command executed successfully
        if result.returncode == 0:
            # Print the output of the command
            print(result.stdout)
        else:
            # Print the error message
            print(result.stderr)


commands_to_execute = [
    "sudo apt install mariadb-server mariadb-client"
]
Install_mariadb_shell_commands(commands_to_execute)

def Install_Redis_shell_commands(commands):
    for command in commands:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Check the return code to see if the command executed successfully
        if result.returncode == 0:
            # Print the output of the command
            print(result.stdout)
        else:
            # Print the error message
            print(result.stderr)


commands_to_execute = [
    "sudo apt-get install redis-server"
]
Install_Redis_shell_commands(commands_to_execute)

def Install_other_package1_shell_commands(commands):
    for command in commands:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Check the return code to see if the command executed successfully
        if result.returncode == 0:
            # Print the output of the command
            print(result.stdout)
        else:
            # Print the error message
            print(result.stderr)


commands_to_execute = [
    "sudo apt-get install xvfb libfontconfig wkhtmltopdf"
]
Install_other_package1_shell_commands(commands_to_execute)

def Install_other_package2_shell_commands(commands):
    for command in commands:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Check the return code to see if the command executed successfully
        if result.returncode == 0:
            # Print the output of the command
            print(result.stdout)
        else:
            # Print the error message
            print(result.stderr)


commands_to_execute = [
    "sudo apt-get install libmysqlclient-dev"
]
Install_other_package2_shell_commands(commands_to_execute)

def Install_MYSQL_Server_shell_commands(commands):
    '''
    Enter current password for root: (Enter your SSH root user password)
    Switch to unix_socket authentication [Y/n]: Y
    Change the root password? [Y/n]: Y
    It will ask you to set new MySQL root password at this step. This can be different from the SSH root user password.
    Remove anonymous users? [Y/n] Y
    Disallow root login remotely? [Y/n]: N
    This is set as N because we might want to access the database from a remote server for using business analytics software like Metabase / PowerBI / Tableau, etc.
    Remove test database and access to it? [Y/n]: Y
    Reload privilege tables now? [Y/n]: Y
    '''
    for command in commands:
        result = subprocess.run(command, shell=True)

        # Check the return code to see if the command executed successfully
        if result.returncode == 0:
            # Print the output of the command
            print(result.stdout)
        else:
            # Print the error message
            print(result.stderr)


commands_to_execute = [
    "sudo mysql_secure_installation"
]
# Install_MYSQL_Server_shell_commands(commands_to_execute)

def Edit_MYSQL_default_config_file(commands):
    for command in commands:
        result = subprocess.run(command, shell=True)

        # Check the return code to see if the command executed successfully
        if result.returncode == 0:
            # Print the output of the command
            print(result.stdout)
        else:
            # Print the error message
            print(result.stderr)

commands_to_execute = [
    "sudo nano /etc/mysql/my.cnf"
]
Edit_MYSQL_default_config_file(commands_to_execute)

# Add the following block of code exactly as is:
'''
    [mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci

[mysql]
default-character-set = utf8mb4

 '''
def Restart_the_MYSQL_Server(commands):
    for command in commands:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Check the return code to see if the command executed successfully
        if result.returncode == 0:
            # Print the output of the command
            print(result.stdout)
        else:
            # Print the error message
            print(result.stderr)

commands_to_execute = [
    "sudo service mysql restart"
]
Restart_the_MYSQL_Server(commands_to_execute)

def Install_CURL(commands):
    for command in commands:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Check the return code to see if the command executed successfully
        if result.returncode == 0:
            # Print the output of the command
            print(result.stdout)
        else:
            # Print the error message
            print(result.stderr)

commands_to_execute = [
    "sudo apt install curl"
]
Install_CURL(commands_to_execute)


def install_nvm_and_node():
    # Command 1: Install NVM and set up environment
    install_nvm_command = '''
        curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.39.5/install.sh | bash &&
        export NVM_DIR="$HOME/.nvm" &&
        [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
    '''
    subprocess.run(install_nvm_command, shell=True, executable="/bin/bash")

    # Command 2: Install Node.js version 16.15.0
    install_node_command = '''
        source "$HOME/.nvm/nvm.sh" && 
        nvm install 16.15.0
    '''
    subprocess.run(install_node_command, shell=True, executable="/bin/bash")

# Call the function to install NVM and Node.js
install_nvm_and_node()


def Install_NPM(commands):
    for command in commands:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Check the return code to see if the command executed successfully
        if result.returncode == 0:
            # Print the output of the command
            print(result.stdout)
        else:
            # Print the error message
            print(result.stderr)

commands_to_execute = [
    "sudo apt-get install npm"
]
Install_NPM(commands_to_execute)

def Install_Yarn(commands):
    for command in commands:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Check the return code to see if the command executed successfully
        if result.returncode == 0:
            # Print the output of the command
            print(result.stdout)
        else:
            # Print the error message
            print(result.stderr)

commands_to_execute = [
    "sudo npm install -g yarn"
]
Install_Yarn(commands_to_execute)

def Install_Frappe_Bench(commands):
    for command in commands:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Check the return code to see if the command executed successfully
        if result.returncode == 0:
            # Print the output of the command
            print(result.stdout)
        else:
            # Print the error message
            print(result.stderr)

commands_to_execute = [
    "sudo pip3 install frappe-bench"
]
Install_Frappe_Bench(commands_to_execute)


def Initialize_Frappe_Bench(commands):
    for command in commands:
        result = subprocess.run(command, shell=True)

        # Check the return code to see if the command executed successfully
        if result.returncode == 0:
            # Print the output of the command
            print(result.stdout)
        else:
            # Print the error message
            print(result.stderr)

commands_to_execute = [
    "bench init --frappe-branch version-14 frappe-bench"
]
Initialize_Frappe_Bench(commands_to_execute)


# #Switch directories into the Frappe Bench directory
# def Switch_directories(commands):
#     for command in commands:
#         result = subprocess.run(command, shell=True)

#         # Check the return code to see if the command executed successfully
#         if result.returncode == 0:
#             # Print the output of the command
#             print(result.stdout)
#         else:
#             # Print the error message
#             print(result.stderr)

# commands_to_execute = [
#     "cd frappe-bench"
# ]
# Switch_directories(commands_to_execute)

# //////////////////////////

# def Create_New_Site(commands):
#     for command in commands:
#         result = subprocess.run(command, shell=True, capture_output=True, text=True)

#         # Check the return code to see if the command executed successfully
#         if result.returncode == 0:
#             # Print the output of the command
#             print(result.stdout)
#         else:
#             # Print the error message
#             print(result.stderr)

# commands_to_execute = [
#     "bench new-site fintech"
# ]
# Create_New_Site(commands_to_execute)


