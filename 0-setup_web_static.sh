#!/usr/bin/env bash
# sets up web servers for the deployment of web_static

# Install HAproxy if not installed
if ! command -v nginx >/dev/null; then
    apt-get -y update
    apt-get -y install nginx
fi

service nginx start

if [ ! -d "/data/web_static/shared/" ]; then
    mkdir -p /data/web_static/shared/
fi

if [ ! -d "/data/web_static/releases/test/" ]; then
    mkdir -p /data/web_static/releases/test/
fi

cat <<EOF > /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
    Realtrailblazer.tech
  </body>
</html>
EOF

if [ -L "/data/web_static/current" ]; then
    rm "/data/web_static/current"
fi

ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

if [ ! -f "/etc/nginx/sites-available/default.bak" ]; then
    cp "/etc/nginx/sites-available/default" "/etc/nginx/sites-available/default.bak"
else
    cp "/etc/nginx/sites-available/default.bak" "/etc/nginx/sites-available/default"
fi

sudo sed -i '/server_name _;/a \\n        location /hbnb_static/ {\n            alias /data/web_static/current/;\n        }' /etc/nginx/sites-available/default

service nginx restart
exit 0
