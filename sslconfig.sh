#!/bin/bash

CONTAINER_ID="prestashop"

docker exec $CONTAINER_ID /var/www/html/ssl/sslconfig.sh