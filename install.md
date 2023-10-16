### PreRequset

- Python 3.10+ (v14)
- Node.js 16
- Redis 6
- MariaDB 10.6.6+ / Postgres v12 to v14
- yarn 1.12+
- pip 20+
- wkhtmltopdf (version 0.12.5 with patched qt)
- cron
- NGINX


### Variables
|var|default|description|
|---|-------|-----------|
| `<db_password>`|  |DATABASE *root* user password|
| `<frappe-bench-path>`   | "$HOME/frappe-bench"|Path for frappe-bench environment|
| `<payments_repo_path>`   |  "https://github.com/fintechsys/payments.git" |   |
| `<erpnext_repo_path>`   |  "https://github.com/fintechsys/erpnext.git" |   |
| `<hrms_repo_path>`   |  "https://github.com/fintechsys/hrms.git" |   |
| `<site_name>`   |   | frappe site name   |
| `<frappe_admin_password>`   |   | password of frappe site **Administrator** user |


### Install
#### Debian / Ubuntu

```sh
sudo apt install git python3-dev python3-pip redis-server
sudo apt install software-properties-common
sudo apt-get update
sudo apt-get install mariadb-server
```


- change Mariadb **root** password:

```sh
sudo mysql <<EOF
DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');
ALTER USER 'root'@'localhost' IDENTIFIED BY "<db_password>"
DROP USER IF EXISTS ''@'localhost';
DROP USER IF EXISTS ''@'$(hostname)';
DROP DATABASE IF EXISTS `test`;
FLUSH PRIVILEGES;
EOF
```

- verify:

```sh
mysql --user=root --password=<db_password> -e "exit"
```

- config MariaDB:

```sh
sudo bash -c "cat >> /etc/mysql/my.cnf <<EOF
[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci

[mysql]
default-character-set = utf8mb4

EOF"

sudo systemctl restart mariadb
```

- verify:

```sh
systemctl status mariadb
```

- install nvm

```sh
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
source ~/.bashrc
```

- verify:

```sh
nvm --version
```

- install Node

```sh
nvm install 16
```

- verify:

```sh
node -v
```

> output should be `v16.x.x` where `x` could be any number

- install yarn

```sh
npm install -g yarn
```

- verify:

```sh
yarn --version
```

- install wkhtmltopdf

```sh
sudo apt-get install xvfb libfontconfig wkhtmltopdf
```

- verify

```sh
wkhtmltopdf --version
```

> can be passed if failed

- install frappe-bench

```sh
pip3 install frappe-bench
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

- verify:

```sh
bench --version
```

### prepare frappe-bench

```sh
# init frappe environment
DIRNAME=$(dirname "<frappe-bench-path>")
FRAPPE_BENCH=$(basename "<frappe-bench-path>")

cd "$DIRNAME"

bench init --frappe-branch version-14 --frappe-path <frappe_repostory_path> "$FRAPPE_BENCH"
```

- verify

```sh
cd "<frappe-bench-path>"
./env/bin/python -m pip show frappe
```

- download & install apps

```sh

cd "<frappe-bench-path>"

# download apps

bench get-app --branch version-14 <payments_repo_path>
bench get-app --branch version-14 <erpnext_repo_path>
bench get-app --branch version-14 <hrms_repo_path>
bench get-app https://github.com/fintechsys/remittance_base.git
bench get-app https://github.com/fintechsys/remittance.git
bench get-app https://github.com/fintechsys/bulk_remittance.git
bench get-app https://github.com/fintechsys/remittance_stellar_integration.git
bench get-app https://github.com/fintechsys/remittance_customize.git
bench get-app https://github.com/fintechsys/client_account_management.git
bench get-app https://github.com/fintechsys/teller_for_erpnext.git
bench get-app https://github.com/fintechsys/teller_for_agent.git
bench get-app https://github.com/fintechsys/rule_management.git
bench get-app https://github.com/fintechsys/payment_management.git
bench get-app https://github.com/fintechsys/remittance_agent_service.git
bench get-app https://github.com/fintechsys/services.git

# make new site

bench new-site --db-root-password=<db_password> --admin-password=<frappe_admin_password> \
--install-app=payments --install-app=erpnext --install-app=hrms <site_name>

# install fintechsys apps

bench --site <site_name> install-app remittance_base remittance bulk_remittance remittance_stellar_integration
bench --site <site_name> install-app client_account_management
bench --site <site_name> install-app teller_for_erpnext teller_for_agent
bench --site <site_name> install-app remittance_customize rule_management payment_management
bench --site <site_name> install-app remittance_agent_service bank_services

```

- verify:

```sh

cd "<frappe-bench-path>"
bench --site <site_name> list-apps
```

> - output format `APPNAME                VERSION             BRANCH` line foreach app
> - apps should contained in output
>   - **frappe**
>   - **payments**
>   - **erpnext**
>   - **hrms**
>   - **remittance_base**
>   - **remittance**
>   - **bulk_remittance**
>   - **remittance_stellar_integration**
>   - **remittance_customize**
>   - **client_account_management**
>   - **teller_for_erpnext**
>   - **teller_for_agent**
>   - **rule_management**
>   - **payment_management**
>   - **remittance_agent_service**
>   - **bank_services**

### prepare production system

in frappe environment folder

```sh
bench setup production
```

```

gosu erpnext bench --site default install-app remittance_base remittance bulk_remittance remittance_stellar_integration
gosu erpnext bench --site default install-app client_account_management
gosu erpnext bench --site default install-app teller_for_erpnext teller_for_agent
gosu erpnext bench --site default install-app remittance_customize rule_management payment_management
gosu erpnext bench --site default install-app remittance_agent_service bank_services
gosu erpnext bench --site default install-app remittance_network_manager

 gosu erpnext gosu erpnext bench
 
 gosu erpnext bench get-app https://github.com/fintechsys/remittance_base.git
gosu erpnext bench get-app https://github.com/fintechsys/remittance.git
gosu erpnext bench get-app https://github.com/fintechsys/bulk_remittance.git
gosu erpnext bench get-app https://github.com/fintechsys/remittance_stellar_integration.git
gosu erpnext bench get-app https://github.com/fintechsys/client_account_management.git
gosu erpnext bench get-app https://github.com/fintechsys/teller_for_erpnext.git
gosu erpnext bench get-app https://github.com/fintechsys/teller_for_agent.git
gosu erpnext bench get-app https://github.com/fintechsys/rule_management.git
gosu erpnext bench get-app https://github.com/fintechsys/payment_management.git
gosu erpnext bench get-app https://github.com/fintechsys/remittance_agent_service.git
gosu erpnext bench get-app https://github.com/fintechsys/services.git
gosu erpnext bench get-app https://github.com/fintechsys/remittance_customize.git


gosu erpnext bench get-app https://github.com/fintechsys/remittance_network_manager.git
```
