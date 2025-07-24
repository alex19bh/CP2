# Indica la imagen que se va a utilizar
FROM --platform=linux/amd64 python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Instala dependencias necesarias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia la app
COPY app.py .
COPY templates/ templates/

# Copia los certificados SSL
COPY clave_publica.crt /app/certs/clave_publica.crt
COPY clave_privada.key /app/certs/clave_privada.key

# Expone el puerto 443
EXPOSE 443

CMD ["python", "app.py"]
