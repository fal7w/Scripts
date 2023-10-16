import subprocess

def install_docker():
    try:
        subprocess.check_call(['sudo', 'apt', 'update'])
        subprocess.check_call(['sudo', 'apt', 'install', '-y', 'docker.io'])
        print('Docker installed successfully.')
    except subprocess.CalledProcessError:
        print('Installation of Docker failed.')

def install_docker_compose():
    try:

        subprocess.check_call(['sudo', 'curl', '-SL', '-o', '/usr/local/bin/docker-compose', 'https://github.com/docker/compose/releases/download/v2.20.3/docker-compose-Linux-x86_64'])
        subprocess.check_call(['sudo', 'chmod', '+x', '/usr/local/bin/docker-compose'])
        print('Docker Compose installed successfully.')
    except subprocess.CalledProcessError:
        print('Installation of Docker Compose failed.')

        # DOCKER_CONFIG = '{DOCKER_CONFIG:-HOME/.docker}';
        # subprocess.check_call(['DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}'])
    #     subprocess.check_call(['mkdir', '-p', '$HOME/.docker/cli-plugins'])
    #     subprocess.check_call(['curl', '-SL', 'https://github.com/docker/compose/releases/download/v2.20.3/docker-compose-linux-x86_64 -o $HOME/.docker/cli-plugins/docker-compose'])
    #     subprocess.check_call(['chmod', '+x', '$HOME/.docker/cli-plugins/docker-compose'])
    #     subprocess.check_call(['docker', 'compose', 'version'])
    #     print('Docker Compose installed successfully.')
    # except subprocess.CalledProcessError:
    #     print('Installation of Docker Compose failed.')

# Execute the installation functions
install_docker()
install_docker_compose()