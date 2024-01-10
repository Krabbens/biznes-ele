FROM prestashop/prestashop:1.7.8-apache

COPY ./dbdump /dbdump

RUN rm -rf /var/www/html/*

COPY ./shop /var/www/html

# remove cache under var/cache/prod and var/cache/dev
RUN rm -rf /var/www/html/var/cache/* && \
    chown -R www-data:www-data /var/www/html && \
    chmod -R 755 /var/www/html

RUN apt-get update && \
    apt-get install -y libmemcached-dev zlib1g-dev && \
    pecl install memcached && \
    docker-php-ext-enable memcached