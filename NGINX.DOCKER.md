

docker build -t nginx-exemplo .

docker run -d -p 8001:80 --name nginx-exemplo nginx-exemplo -v [volume-name] /var/www/html