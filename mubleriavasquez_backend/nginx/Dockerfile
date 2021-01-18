FROM nginx 
COPY default.conf /etc/nginx/default.conf
COPY ./uwsgi_params /etc/nginx/uwsgi_params

EXPOSE 8080 
CMD ["nginx","-g","daemon off;"] 

