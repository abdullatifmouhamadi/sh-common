# installing prestashop

```

sudo pacman -S geoip ca-certificates git tzdata zip
sudo pacman -S nginx-mod-headers-more nginx-mod-geoip2

sudo pacman -S libmcrypt zlib gmp freetype2 libjpeg-turbo libpng

sudo pacman -S musl mariadb-clients

```


```
/etc/php72/php.ini

mysqli
gd
pdo_mysql
intl
iconv

```



```
https://websiteforstudents.com/how-to-install-prestashop-on-ubuntu-20-04-18-04-with-nginx-and-lets-encrypt/
```


## yay
```
yay -S php72-fpm php72-imagick php72-gd php72-mcrypt php72-apcu php72-apcu-bc php72-memcached php72-intl 

```

## conf
```

find /usr/html/ -type f -exec chmod 644 {} \; && find /usr/html/ -type d -exec chmod 755 {} \;


find /home/abdullatif/apps/prestashop_1.7.6.7/prestashop/ -type f -exec chmod 644 {} \; && find /home/abdullatif/apps/prestashop_1.7.6.7/prestashop/ -type d -exec chmod 755 {} \;

sudo chown -R http:http /home/abdullatif/apps/prestashop_1.7.6.7/prestashop/

```


