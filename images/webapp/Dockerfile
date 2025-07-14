FROM docker.io/library/nginx:latest

# Instalar apache2-utils para htpasswd
RUN apt-get update && apt-get install -y apache2-utils && rm -rf /var/lib/apt/lists/*

# Copiamos el index a la carpeta de nginx
COPY index.html /usr/share/nginx/html/index.html

# Creamos archivo de autenticación
RUN htpasswd -bc /etc/nginx/.htpasswd alex alex123

# Configuramos autenticación en nginx
RUN echo 'server {\n\
    listen 80;\n\
    location / {\n\
        auth_basic "Restricted";\n\
        auth_basic_user_file /etc/nginx/.htpasswd;\n\
        root /usr/share/nginx/html;\n\
    }\n\
}' > /etc/nginx/conf.d/default.conf
