
"""
@file app.py
@brief Aplicacion web Flask.
@details Aplicacion de ejemplo para la actividad de monitorizacion.
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    """
    @brief Muestra el mensaje principal.
    @return Mensaje indicando que Flask funciona correctamente.
    """
    return "Aplicacion Flask funcionando correctamente con Docker"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
