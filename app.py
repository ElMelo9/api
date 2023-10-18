from flask import Flask
import logging
from src.routes.getRoutes import get_routes
from src.routes.postRoutes import post_routes

app = Flask(__name__)
# Configura la ubicación de los registros en la carpeta "log"
logging.basicConfig(filename='src/log/app.log', level=logging.DEBUG)

# Registra las rutas GET
app.register_blueprint(get_routes)

# Registra las rutas POST
app.register_blueprint(post_routes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
