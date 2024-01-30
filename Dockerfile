FROM nginx
COPY html /usr/share/nginx/html
COPY deep-start.sh /usr/local/bin/deep-start
RUN chmod +x /usr/local/bin/deep-start
ENTRYPOINT [ "deep-start" ]