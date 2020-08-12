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

## install
```

cd /tmp
wget https://download.prestashop.com/download/releases/prestashop_1.7.6.5.zip
unzip prestashop_*.zip


sudo mkdir -p /srv/http/prestashop
sudo unzip prestashop.zip -d /srv/http/prestashop


sudo chown -R http:http /srv/http/prestashop
sudo chmod -R 755 /srv/http/prestashop



```


