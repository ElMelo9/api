from flask import Blueprint

get_routes = Blueprint('get_routes', __name__)

@get_routes.route('/')
def get_hello_world():
    from app import app  # Importa la aplicación aquí para evitar la importación circular
    app.logger.info('Se ha recibido una solicitud GET en la ruta /')
    return '¡Hola, mundo (GET)!'
