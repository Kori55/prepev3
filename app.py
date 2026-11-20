from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total de solicitudes HTTP recibidas'
)

@app.route("/")
def inicio():
    REQUEST_COUNT.inc()
    return "Aplicacion Flask funcionando correctamente con Docker"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
