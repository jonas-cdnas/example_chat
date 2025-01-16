# Usar una imagen base ligera de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY requirements.txt /app/requirements.txt
COPY app.py /app/app.py

# Instalar las dependencias
RUN apt-get update && apt-get install -y \
    build-essential gcc libffi-dev libssl-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el contenedor
EXPOSE 9000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]