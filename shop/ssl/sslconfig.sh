#!/bin/bash

# Ścieżka do pliku default-ssl.conf w kontenerze
CONFIG_PATH="/etc/apache2/sites-available/default-ssl.conf"

# Nowe ścieżki do klucza i certyfikatu
NEW_KEY_PATH="/var/www/html/ssl/localhost.key"
NEW_CERT_PATH="/var/www/html/ssl/localhost.crt"

# Zmień ścieżki w pliku default-ssl.conf
sed -i "s|SSLCertificateKeyFile.*|SSLCertificateKeyFile $NEW_KEY_PATH|" $CONFIG_PATH
sed -i "s|SSLCertificateFile.*|SSLCertificateFile $NEW_CERT_PATH|" $CONFIG_PATH
a2enmod ssl
a2ensite default-ssl.conf

# Zrestartuj serwer Apache
service apache2 restart

echo "Zmieniono ścieżki do klucza i certyfikatu w pliku default-ssl.conf w kontenerze."