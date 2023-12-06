#!/bin/bash

docker-compose up -d

chmod -R 777 shop 

chmod -R 777 dbdump

docker exec adidas-mariadb-server /var/lib/dbdump/import.sh

docker exec prestashop /var/www/html/ssl/sslconfig.sh