# API de ejemplo con Flask

API mínima con un endpoint `GET /greet` que devuelve texto plano:

- `/greet?name=Ana` → `Hello Ana!`
- `/greet` → `Hello World!`
- `/greet?name=` → `Hello !` (el valor por defecto se usa solo si falta el parámetro).

## Requisitos

Linux, Python 3.12 o superior y [uv](https://docs.astral.sh/uv/getting-started/installation/).
Ejecuta los comandos desde el directorio del proyecto.

## Instalar y ejecutar con uv

```bash
uv sync --locked
uv run flask --app app run
```

La API estará disponible en `http://127.0.0.1:5000`. El servidor incluido en
Flask está pensado para desarrollo local.

```bash
curl "http://127.0.0.1:5000/greet?name=Ana"
# Hello Ana!

curl "http://127.0.0.1:5000/greet"
# Hello World!
```

## Ejecutar con Gunicorn

Para servir la API en producción, utiliza Gunicorn, incluido en las
dependencias de la aplicación:

```bash
uv sync --locked --no-dev
uv run --no-dev gunicorn --bind 0.0.0.0:8000 app:app
```

`app:app` indica el módulo `app.py` y la instancia Flask `app`.
El servidor escucha en todas las interfaces en el puerto 8000:

```bash
curl "http://127.0.0.1:8000/greet?name=Ana"
# Hello Ana!
```

Si has instalado las dependencias con pip, ejecuta lo siguiente con el
entorno virtual activado:

```bash
gunicorn --bind 0.0.0.0:8000 app:app
```

## Tests

`pytest` está declarado en el grupo de dependencias `dev`, que `uv sync`
instala por defecto.

```bash
uv run python -m pytest
```

## Generar requirements para clientes sin uv

`pyproject.toml` declara las dependencias y `uv.lock` fija sus versiones.
Los dos ficheros exportados están incluidos para poder instalar con pip.
Para regenerarlos con uv:

```bash
uv export --locked --no-dev --no-hashes --output-file requirements.txt
uv export --locked --only-dev --no-hashes --output-file requirements-dev.txt
```

`requirements.txt` incluye Flask, Gunicorn y sus dependencias. `requirements-dev.txt`
incluye únicamente pytest y sus dependencias. Para desarrollar y ejecutar
los tests, instala ambos ficheros.
Si modificas las dependencias en `pyproject.toml`, ejecuta `uv lock` antes
de regenerar ambos ficheros.

## Instalar y ejecutar sin uv

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m flask --app app run
```

Si tu sistema utiliza `python3` en lugar de `python`, úsalo al crear el entorno.

Para instalar las dependencias de desarrollo y ejecutar los tests sin uv,
con el entorno activado:

```bash
python -m pip install -r requirements.txt -r requirements-dev.txt
python -m pytest
```

Referencias: [Flask](https://flask.palletsprojects.com/en/stable/quickstart/),
[Gunicorn](https://gunicorn.org/run/)
y [exportación de dependencias con uv](https://docs.astral.sh/uv/concepts/projects/export/).
