FROM nginx:1.15

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d

COPY index.html /var/www/html/

# Indica onde o volume será montado
# VOLUME /var/www/html/