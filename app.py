from flask import Flask, Response, request

app = Flask(__name__)


@app.get("/greet")
def greet():
    name = request.args.get("name", "World")
    return Response(f"Hello {name}!", mimetype="text/plain")
