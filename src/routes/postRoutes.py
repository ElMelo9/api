import datetime
from database.crud_operations import Crud
from services.authLogin import AuthUser
from services.authToken import verificar_token
from services.summary import SummaryText
from services.traslate import Translate
from flask import Blueprint, request, jsonify
import jwt
import os
import sys
# Obtén la ruta del directorio actual
current_directory = os.path.dirname(os.path.realpath(__file__))
# Agrega el directorio raíz de tu proyecto al sys.path
project_directory = os.path.abspath(os.path.join(current_directory, '..'))
sys.path.append(project_directory)

crud = Crud()


post_routes = Blueprint('post_routes', __name__)

# Ruta para login
@post_routes.route('/login', methods=['POST'])
def login():
    auth = AuthUser()
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos de login no proporcionados"}), 400
    # credenciales
    email = data.get("email")
    password = data.get ("password")
    if not email or not password:
        return jsonify({"error": "datos incompletos para login!"}), 400
    # Llama a la función create_role para crear el rol en Supabase
    
    if auth.validate_credentials(email,password):
        info = {
    'email': email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60)  # Vence en 30 minutos
    }
        # Si las credenciales son válidas, genera un token JWT
        token = jwt.encode(info,"tuvrj_XPb:?jnm(Yn[4X&Lc%$iiR`/n4FX?s1'Vh94Apy.j>?v", algorithm='HS256')
        return jsonify({'token': token}),201
    else:
        return jsonify({'mensaje': 'Credenciales incorrectas'}), 401


# Ruta para crear un rol
@post_routes.route('/crear_rol', methods=['POST'])
def crear_rol():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos del rol no proporcionados"}), 400
    # Nombre del rol a crear
    nombre_rol = data.get("nombre_rol")
    if not nombre_rol:
        return jsonify({"error": "Nombre de rol no proporcionado"}), 400
    # Llama a la función create_role para crear el rol en Supabase
    result = crud.create_role(data)
    if isinstance(result, Exception):
        return jsonify({"error": str(result)}), 500
    return jsonify({"message": f"Rol '{nombre_rol}' creado correctamente"}), 201


# Ruta para crear un tipo documento
@post_routes.route('/crear_document', methods=['POST'])
def crear_document():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos del tipo documento no proporcionados"}), 400
    # Nombre del rol a crear
    identificacion = data.get("identificacion")
    sigla = data.get("sigla")
    if not identificacion or not sigla:
        return jsonify({"error": "Nombre de tipo documento  o sigla no proporcionado"}), 400
    # Llama a la función create_role para crear el rol en Supabase
    result = crud.create_document(data)
    if isinstance(result, Exception):
        return jsonify({"error": str(result)}), 500
    return jsonify({"message": f"tipo documento '{identificacion}' y sigla '{sigla}' creado correctamente"}), 201


# Ruta para crear un usuario
@post_routes.route('/crear_usuario', methods=['POST'])
#@verificar_token
def crear_usuario():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos del usuario no proporcionados"}), 400
    # validar datos

    id_rol = data.get("id_rol")
    id_documento= data.get("id_documento")
    num_doc= data.get("num_doc")
    nombre= data.get("nombre")
    apellido= data.get("apellido")
    email= data.get("email")
    password= data.get("password")
    if not id_rol or not id_documento or not num_doc or not nombre or not apellido or not email or not password:
        return jsonify({"error": "faltan datos para crear el usuario"}), 400
    # Llama a la función create_role para crear el rol en Supabase
    result = crud.create_user(data)
    if isinstance(result, Exception):
        return jsonify({"error": str(result)}), 500
    return jsonify({" message": f" usuario creado correctamente"}), 201

# Ruta para crear un traducciones
@post_routes.route('/crear_traduccion', methods=['POST'])
def crear_traduccion():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos del usuario no proporcionados"}), 400
    # validar datos

    id_usuario = data.get("id_usuario")
    text_traduccion= data.get("text_traduccion")
    text_resumen= data.get("text_resumen")
    text_traducido= data.get("text_traducido")
    if not id_usuario or not text_traduccion or not text_resumen or not text_traducido:
        return jsonify({"error": "faltan datos para crear el usuario"}), 400
    # Llama a la función create_role para crear el rol en Supabase
    result = crud.create_translations(data)
    if isinstance(result, Exception):
        return jsonify({"error": str(result)}), 500
    return jsonify({" message": f" traducciones creado correctamente"}), 201

# Ruta para crear un historial_chat
@post_routes.route('/crear_historialChat', methods=['POST'])
def crear_historialChat():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos del usuario no proporcionados"}), 400
    # validar datos

    id_usuario = data.get("id_usuario")
    fecha_historial= data.get("fecha_historial")
    chat_usuario= data.get("chat_usuario")
    if not id_usuario or not fecha_historial or not chat_usuario:
        return jsonify({"error": "faltan datos para crear el usuario"}), 400
    # Llama a la función create_role para crear el rol en Supabase
    result = crud.create_chatHistory(data)
    if isinstance(result, Exception):
        return jsonify({"error": str(result)}), 500
    return jsonify({" message": f" historial_chat creado correctamente"}), 201

# Ruta para crear un contactenos
@post_routes.route('/crear_contactenos', methods=['POST'])
def crear_contactenos():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos del usuario no proporcionados"}), 400
    # validar datos

    id_usuario = data.get("id_usuario")
    fecha_historial= data.get("fecha_historial")
    chat_usuario= data.get("chat_usuario")
    if not id_usuario or not fecha_historial or not chat_usuario:
        return jsonify({"error": "faltan datos para crear el usuario"}), 400
    # Llama a la función create_role para crear el rol en Supabase
    result = crud.create_ContactUs(data)
    if isinstance(result, Exception):
        return jsonify({"error": str(result)}), 500
    return jsonify({" message": f" contactenos creado correctamente"}), 201

# Ruta para resumir y traducir
@post_routes.route('/resumirTraducir', methods=['POST'])
def resumirTraducirs():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos del usuario no proporcionados"}), 400
    # validar datos

    text = data.get("text")
    if not text :
        return jsonify({"error": "falta texto para resumir y traducir"}), 400
    resumir = SummaryText()
    result = resumir.generate_summary(text,3)
    traducir = Translate()
    result2 = traducir.translador(result)
    if isinstance(result, Exception):
        return jsonify({"error": str(result)}), 500
    return jsonify({" resumen": result,"traducido":result2}), 201
