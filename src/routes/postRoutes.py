from flask import Blueprint, request, jsonify
from database.crud_operations import create_role  # Importa la función create_role

post_routes = Blueprint('post_routes', __name__)

# Ruta para crear un rol
@post_routes.route('/crear_rol', methods=['POST'])
def crear_rol():
    # Obtener los datos del rol desde el cuerpo de la solicitud
    data = request.get_json()

    if not data:
        return jsonify({"error": "Datos del rol no proporcionados"}), 400

    # Nombre del rol a crear
    nombre_rol = data.get("nombre_rol")

    if not nombre_rol:
        return jsonify({"error": "Nombre de rol no proporcionado"}), 400

    # Llama a la función create_role para crear el rol en Supabase
    result = create_role('tu_tabla_de_roles', data)

    if isinstance(result, Exception):
        return jsonify({"error": str(result)}), 500

    return jsonify({"message": f"Rol '{nombre_rol}' creado correctamente"}), 201
