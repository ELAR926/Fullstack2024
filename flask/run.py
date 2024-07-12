# run.py

from flask import Flask
from flask_cors import CORS
from app.views import *
from app.database import *

app = Flask(__name__)

# Definición de funciones de vistas
app.route('/api/tasks/reservas', methods=['GET'])(mostrar_formulario)
app.route('/api/tasks/reservas', methods=['POST'])(procesar_formulario)

# Configuración de la base de datos
init_app(app)

# Configuración de CORS
CORS(app)

# Manejo de errores 404


@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    test_connection()  # Verificar conexión a la base de datos al iniciar la aplicación
    app.run(debug=True)
