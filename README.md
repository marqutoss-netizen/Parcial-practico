# Galería Docker

Aplicación web en **Flask (Python)** que muestra una galería de imágenes, contenerizada con **Docker**.
Proyecto del examen de Docker – Ingeniería de Software, Uniempresarial.

> El objetivo del proyecto es el proceso de contenerización, no la complejidad de la app.

## Estructura

```
galeria-docker/
├── app.py              # Aplicación Flask
├── templates/
│   └── index.html      # Plantilla de la galería
├── static/img/         # Imágenes que muestra la galería
├── requirements.txt    # Dependencias de Python
├── Dockerfile          # Receta para construir la imagen
└── .dockerignore       # Archivos que no se copian a la imagen
```

## Requisitos

- Docker instalado y en ejecución (`docker --version` debe responder).
- Git (para clonar el repositorio).

## Reproducir paso a paso

### 1. Clonar el repositorio

```bash
git clone https://github.com/marqutoss-netizen/galeria-docker.git
cd galeria-docker
```

### 2. Construir la imagen

```bash
docker build -t galeria-app:1.0 .
```

- `build`: construye una imagen a partir del Dockerfile.
- `-t galeria-app:1.0`: le pone nombre (`galeria-app`) y etiqueta/versión (`1.0`).
- `.`: contexto de construcción (la carpeta actual, donde está el Dockerfile).

Verificar que la imagen existe:

```bash
docker images
```

### 3. Ejecutar el contenedor

```bash
docker run -d --name galeria -p 8080:5000 galeria-app:1.0
```

- `-d`: modo *detached* (segundo plano).
- `--name galeria`: nombre del contenedor, para manejarlo fácilmente.
- `-p 8080:5000`: publica el puerto 5000 del contenedor en el puerto 8080 de tu máquina (`host:contenedor`).
- `galeria-app:1.0`: imagen a usar.

Comprobar que está corriendo:

```bash
docker ps
```

### 4. Abrir la aplicación

Entrar en el navegador a **http://localhost:8080**. Debe verse la galería con las imágenes.

Ver los registros de la aplicación:

```bash
docker logs galeria
```

### 5. Detener el contenedor

```bash
docker stop galeria
docker ps -a
```

`docker ps` ya no lo lista; `docker ps -a` lo muestra con estado `Exited`.
Al recargar http://localhost:8080 el navegador **no puede conectarse**: la aplicación no está disponible.

### 6. Reiniciar el contenedor

```bash
docker start galeria
docker ps
```

Al recargar http://localhost:8080 la aplicación **vuelve a funcionar**.

### 7. Limpieza (opcional)

```bash
docker stop galeria
docker rm galeria
docker rmi galeria-app:1.0
```

## Problemas comunes y soluciones

| Problema | Causa | Solución |
|---|---|---|
| El contenedor corre pero el navegador no carga la app | Flask escuchaba en `127.0.0.1` dentro del contenedor, inalcanzable desde fuera | Usar `app.run(host="0.0.0.0")` |
| `port is already allocated` / `address already in use` | El puerto 8080 del host ya lo usa otro proceso o contenedor | Cambiar el puerto del host (`-p 8081:5000`) o detener el otro contenedor |
| `The container name "/galeria" is already in use` | Ya existe un contenedor con ese nombre | `docker rm galeria` y volver a ejecutar `docker run` |
| `Cannot connect to the Docker daemon` | Docker no está iniciado | Abrir Docker Desktop o `sudo systemctl start docker` |

## Variables de entorno

- `PORT`: puerto interno de la aplicación (por defecto `5000`).
  Ejemplo: `docker run -d -p 8080:6000 -e PORT=6000 galeria-app:1.0`
