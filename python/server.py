import random
from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

# Clave para manejar sesiones en Flask
app.secret_key = "clave_secreta"

# Lista de predicciones para el juego
lista_predicciones = [
    "Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría.",
    "Un gran cambio laboral o académico llegará pronto. Estás preparado para ganar.",
    "Un viaje inesperado te revelará un secreto valioso sobre tu camino."
]

# Ruta principal que muestra el formulario para ingresar datos
@app.route('/')
def formulario_principal():
    return render_template('index.html')

#

if __name__ == "__main__":
    app.run(debug=True)