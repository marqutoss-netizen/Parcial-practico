import os

from flask import Flask, render_template

app = Flask(__name__)

IMG_DIR = os.path.join(app.static_folder, "img")
EXTENSIONES = (".jpg", ".jpeg", ".png", ".gif", ".webp")


def listar_imagenes():
    archivos = sorted(f for f in os.listdir(IMG_DIR) if f.lower().endswith(EXTENSIONES))
    return [
        {"archivo": f, "titulo": os.path.splitext(f)[0].split("-", 1)[-1].capitalize()}
        for f in archivos
    ]


@app.route("/")
def home():
    return render_template("index.html", imagenes=listar_imagenes())


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    # host 0.0.0.0 es obligatorio dentro de un contenedor:
    # con 127.0.0.1 la app solo seria accesible desde dentro del propio contenedor.
    puerto = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=puerto)
