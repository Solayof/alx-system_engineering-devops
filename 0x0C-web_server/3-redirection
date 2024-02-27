#!/usr/bin/env bash
#Configure nginx server so that /redirect_me is redirecting to another page.


sudo apt-get -y update
sudo apt-get -y install -y nginx
sudo ufw allow 'Nginx HTTP'
echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html
sudo sed -i '/listen 80 default_server/a \    location /redirect_me { \n        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent; \n    }' /etc/nginx/sites-available/default
sudo service nginx reload
