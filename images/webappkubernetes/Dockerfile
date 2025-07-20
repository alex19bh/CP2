FROM --platform=linux/amd64 docker.io/library/nginx:latest

# Instalar apache2-utils para htpasswd
RUN apt-get update && apt-get install -y apache2-utils && rm -rf /var/lib/apt/lists/*

# Copiar el archivo index.html a la ruta de NGINX
COPY index.html /usr/share/nginx/html/index.html

# Crear archivo de autenticación
RUN htpasswd -bc /etc/nginx/.htpasswd alex alex123

# Crear directorio de certificados
RUN mkdir -p /etc/nginx/certs

# Copiar certificados TLS (asegúrate de tener los archivos cert.pem y key.pem en ./certs)
COPY clave_publica.crt /etc/nginx/certs/clave_publica.crt
COPY clave_privada.key /etc/nginx/certs/clave_privada.key

# Configuración de NGINX para HTTPS + autenticación
RUN echo '\
server {\n\
    listen 443 ssl;\n\
    ssl_certificate /etc/nginx/certs/clave_publica.crt;\n\
    ssl_certificate_key /etc/nginx/certs/clave_privada.key;\n\
\n\
    location / {\n\
        auth_basic "Restricted";\n\
        auth_basic_user_file /etc/nginx/.htpasswd;\n\
        root /usr/share/nginx/html;\n\
        index index.html;\n\
    }\n\
}' > /etc/nginx/conf.d/default.conf

EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]
