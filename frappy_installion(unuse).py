import subprocess
import os

# # Update and upgrade system
subprocess.check_call(['sudo', 'apt-get', 'update'])
subprocess.check_call(['sudo', 'apt-get', 'upgrade'])
# Install required packages
subprocess.run(["sudo", "apt", "install", "git", "python3-dev", "python3-pip", "redis-server"])
subprocess.run(["sudo", "apt", "install", "software-properties-common"])
subprocess.run(["sudo", "apt-get", "install", "mariadb-server"])
print('Install required packages complete ..')


# Change MariaDB root password
mysql_commands = """
DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');
ALTER USER 'root'@'localhost' IDENTIFIED BY "root";
DROP USER IF EXISTS ''@'localhost';
DROP USER IF EXISTS ''@'$(hostname)';
DROP DATABASE IF EXISTS `test`;
FLUSH PRIVILEGES;
"""

# Execute the MySQL commands using the subprocess module
process = subprocess.Popen(['sudo', 'mysql', '-p', '--verbose'], stdin=subprocess.PIPE)
process.communicate(input=mysql_commands.encode())

# Configure MariaDB
# Define the command
command = r"""sudo bash -c "cat >> /etc/mysql/my.cnf <<EOF
[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci

[mysql]
default-character-set = utf8mb4

EOF" """

# Execute the command using the subprocess module
process = subprocess.Popen(command, shell=True)
process.wait()
subprocess.run(["sudo", "systemctl", "restart", "mariadb"])
print(' Configure MariaDB Complete..')

# Install nvm
install_nvm_command = 'curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash'
try:
    subprocess.run(install_nvm_command, shell=True, executable="/bin/bash", check=True)
    print("NVM installation successful.")
except subprocess.CalledProcessError as e:
    print("NVM installation failed:", e)

# Source NVM script to activate it in the current shell
source_nvm_command = 'source ~/.nvm/nvm.sh && source ~/.nvm/bash_completion && nvm ls-remote'
try:
    result = subprocess.run(source_nvm_command, shell=True, executable="/bin/bash", capture_output=True, text=True, check=True)
    print("Available Node.js versions:")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print("Failed to get available Node.js versions:", e)

# Install a different version of Node.js
node_version = "16.0"  # Replace with the desired Node.js version
install_node_command = f'source ~/.nvm/nvm.sh && nvm install {node_version}'
try:
    subprocess.run(install_node_command, shell=True, executable="/bin/bash", check=True)
    print(f"Node.js {node_version} installation successful.")
except subprocess.CalledProcessError as e:
    print(f"Node.js {node_version} installation failed:", e)  

def execute_explore(commands):
    for command in commands:
        try:
            subprocess.run(command, shell=True, executable="/bin/bash", check=True)
            print(f"Command executed successfully: {command}")
        except subprocess.CalledProcessError as e:
            print(f"Command failed: {command}", e)

commands = [
    'export NVM_DIR="$HOME/.nvm"',
    '[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"',
    '[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"'
]

execute_explore(commands)


# Install yarn
subprocess.run(["npm", "install", "-g", "yarn"])
print('Install yarn Complete..')

# Install wkhtmltopdf
subprocess.run(["sudo", "apt-get", "install", "xvfb", "libfontconfig", "wkhtmltopdf"])
print('Install wkhtmltopdf Complete..')

# Install frappe-bench
install_command = 'pip3 install frappe-bench'
try:
    subprocess.run(install_command, shell=True, check=True)
    print("frappe-bench installation successful.")
except subprocess.CalledProcessError as e:
    print("frappe-bench installation failed:", e)

# Append line to ~/.bashrc
append_command = 'echo \'export PATH="$HOME/.local/bin:$PATH"\' >> ~/.bashrc'
try:
    subprocess.run(append_command, shell=True, check=True)
    print("Line appended to ~/.bashrc.")
except subprocess.CalledProcessError as e:
    print("Failed to append line to ~/.bashrc:", e)

# Source ~/.bashrc
source_command = 'source ~/.bashrc'
try:
    subprocess.run(source_command, shell=True, executable="/bin/bash", check=True)
    print("Sourcing ~/.bashrc successful.")
except subprocess.CalledProcessError as e:
    print("Failed to source ~/.bashrc:", e)

   
# Verify installations
print('bennch Version :')
subprocess.run(["bench", "--version"])
source_nvm_command = 'source ~/.nvm/nvm.sh && nvm --version'
try:
    result = subprocess.run(source_nvm_command, shell=True, executable="/bin/bash", capture_output=True, text=True, check=True)
    nvm_version = result.stdout.strip()
    print(f"NVM version: {nvm_version}")
except subprocess.CalledProcessError as e:
    print("Failed to get NVM version:", e)
print('node Version :')
subprocess.run(["node", "-v"])
print('yarn Version :')
subprocess.run(["yarn", "--version"])
print('wkhtmltopdf Version :')
subprocess.run(["wkhtmltopdf", "--version"])