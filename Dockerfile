FROM nginx

COPY default.conf /etc/nginx/conf.d/default.conf
COPY html /usr/share/nginx/html
COPY deep-start.sh /usr/local/bin/deep-start
RUN chmod +x /usr/local/bin/deep-start

EXPOSE 5000
ENTRYPOINT [ "deep-start" ]