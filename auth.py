from flask import Flask, request, jsonify

import jwt
import datetime
from functools import wraps
from os import getenv

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        
        try:
            data = jwt.decode (token, getenv("SECRET"), "HS256")
        except:
            return jsonify({'message': 'Token is invalid',
                            'Key':getenv("SECRET")}), 403

        return f(*args, **kwargs)
    return decorated


def autenticacion(usuario, contrasenia):
    verificacion=False
    perfil="ciudadano"
    if usuario and usuario=="Santy":
        if contrasenia and contrasenia=="san":
            verificacion = True
            perfil = 'titular'
    return {'verificacion':verificacion,
                            'perfil':perfil}

def genera_token(usuario, contrasenia):
    data = autenticacion(usuario, contrasenia)
    access_token = None
    expires_in = None

    if data['verificacion']:
        expires_in = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
        access_token = jwt.encode (payload={'user': usuario, 'exp': expires_in}, 
                            key=getenv("SECRET"))
    return access_token

def obten_tiempo_expiracion(access_token):
    expires_in=None
    if access_token:
        data = jwt.decode (access_token, getenv("SECRET"), "HS256")
        expires_in=data['exp']
    return expires_in