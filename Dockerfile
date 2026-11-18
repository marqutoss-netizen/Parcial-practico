# Imagen base: Python 3.12 en version "slim" (ligera, ~120 MB)
FROM python:3.12-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Se copia primero solo requirements.txt para aprovechar la cache de capas:
# si el codigo cambia pero las dependencias no, pip install no se vuelve a ejecutar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ahora si se copia el resto del proyecto (app.py, templates, static/img)
COPY . .

# Documenta el puerto en el que escucha la aplicacion (no lo publica por si solo)
EXPOSE 5000

# Comando que se ejecuta al iniciar el contenedor
CMD ["python", "app.py"]
