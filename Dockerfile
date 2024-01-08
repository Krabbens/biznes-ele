FROM prestashop/prestashop:1.7.8-apache

COPY ./dbdump /dbdump

RUN rm -rf /var/www/html/*

COPY ./shop /var/www/html

RUN rm -rf /var/www/html/var/cache/* && \
    chown -R www-data:www-data /var/www/html && \
    chmod -R 777 /var/www/html/