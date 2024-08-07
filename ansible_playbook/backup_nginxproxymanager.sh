#!/bin/bash

# Variables
BACKUP_PATH="/root/nginxproxy_backup/nginxproxymanager"
DATE=$(date +"%Y%m%d_%H%M%S")

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_PATH

# Backup data and letsencrypt directories
tar -czvf $BACKUP_PATH/data_backup_$DATE.tar.gz -C ~/devops/stage-ops/nginxproxymanager/data .
tar -czvf $BACKUP_PATH/letsencrypt_backup_$DATE.tar.gz -C ~/devops/stage-ops/nginxproxymanager/letsencrypt .

# Print a message
echo "Nginx Proxy Manager backups completed and stored in $BACKUP_PATH"
