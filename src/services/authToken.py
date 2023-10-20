from flask import request, jsonify
import jwt

def verificar_token(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'mensaje': 'Token no proporcionado'}), 401
        
        if token.startswith('Bearer '):
            token = token[7:]  # Elimina los primeros 7 caracteres (el prefijo "Bearer ")


        try:
            data = jwt.decode(token, "tuvrj_XPb:?jnm(Yn[4X&Lc%$iiR`/n4FX?s1'Vh94Apy.j>?v", algorithms=['HS256'])
            return func(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify({'mensaje': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'mensaje': 'Token no válido'}), 401

    return wrapper
