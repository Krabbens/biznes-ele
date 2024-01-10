#!/bin/bash

#    ^zcie      ka do pliku default-ssl.conf w kontenerze
CONFIG_PATH="/etc/apache2/sites-available/default-ssl.conf"

# Nowe    ^{cie      ki do klucza i certyfikatu
NEW_KEY_PATH="/var/www/html/ssl/localhost.key"
NEW_CERT_PATH="/var/www/html/ssl/localhost.crt"

# Zmie   ^d    ^{cie      ki w pliku default-ssl.conf
sed -i "s|SSLCertificateKeyFile.*|SSLCertificateKeyFile $NEW_KEY_PATH|" $CONFIG_PATH
sed -i "s|SSLCertificateFile.*|SSLCertificateFile $NEW_CERT_PATH|" $CONFIG_PATH
a2enmod ssl
a2ensite default-ssl.conf

echo "drop db"
mysql -hdb -P3306 -uroot -pstudent -e "DROP DATABASE BE_188587;"
echo "create db"
mysql -hdb -P3306 -uroot -pstudent -e "CREATE DATABASE IF NOT EXISTS BE_188587;"
echo "load db"
mysql -hdb -P3306 -uroot -pstudent BE_188587 < /dbdump/adidas-mariadb.sql

exec apache2-foreground