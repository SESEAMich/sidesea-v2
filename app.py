from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, make_response

import jwt
import datetime
from functools import wraps
from os import getenv

from auth import token_required, autenticacion, genera_token, obten_tiempo_expiracion

app = Flask(__name__)
app.config['SECRET_KEY']=getenv("SECRET")

def create_app():
    app = Flask(__name__)
    return app

@app.route('/')
def inicio():
    datos = {'titulo': getenv('TITULO_INICIO')}
    return render_template('index.html', datos=datos)

@app.route('/servidor')
def servidor():
    titulo = 'Datos del Servidor Público'
    datos = {'titulo': titulo}
    return render_template('form-servidor.html', datos=datos)
    
@app.route('/hechos')
def hechos():
    titulo = 'Narración de los hechos'
    datos = {'titulo': titulo,
             'filacion':'no'}
    return render_template('form-hechos.html', datos=datos)

@app.route('/responsable')
def responsable():
    titulo = 'Narración de los hechos'
    datos = {'titulo': titulo,
             'filacion':'si'}
    return render_template('form-hechos.html', datos=datos)

@app.route('/denuncia_enviar')
def denuncia_enviar():
    titulo = 'Enviar denuncia'
    datos = {'titulo': titulo}
    return render_template('denuncia-enviar.html', datos=datos)

@app.route('/denuncia-acuse')
def denuncia_acuse():
    titulo = 'Folio de la denuncia'
    datos = {'titulo': titulo}
    return render_template('denuncia-acuse.html', datos=datos)

@app.route('/consulta')
def consulta():
    titulo = 'Consulta'
    datos = {'titulo': titulo}
    return render_template('consulta.html', datos=datos)

@app.route('/denuncia-detalle')
def detalles():
    titulo = 'detalless'
    folio = '0002-20230415-QSH27'
    datos = {'titulo': titulo,
             'folio': folio}
    return render_template('denuncia-detalle.html', datos=datos)

@app.route('/denuncia-resumen')
def resumen():
    titulo = 'resumen'
    datos = {'titulo': titulo}
    return render_template('denuncia-resumen.html', datos=datos)

@app.route('/registro')
def registro():
    titulo = 'Consulta'
    return "Registro"

@app.route('/preguntas')
def preguntas():
    titulo = 'preguntas'
    datos = {'titulo': titulo}
    return render_template('preguntas.html', datos=datos)

@app.route('/consulta-faltas')
def consulta_faltas():
    titulo = 'Faltas Administrativas graves y no graves'
    datos = {'titulo': titulo, 'tipo':'faltas'}
    return render_template('consulta-faltas-delitos.html', datos=datos)

@app.route('/consulta-delitos')
def consulta_delitos():
    titulo = 'Delitos por hechos de corrupción'
    datos = {'titulo': titulo, 'tipo':'delitos'}
    return render_template('consulta-faltas-delitos.html', datos=datos)


@app.route('/login-1')
def login_1():
    auth = request.authorization
    if auth and auth.password == 'sans':
        token = jwt.encode (payload={'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 
                            key=app.config['SECRET_KEY'])
        return jsonify({'token': token})
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

@app.route("/login", methods=['POST', 'GET'])
def login():

    if not request.form['usuario'] or not request.form['contrasenia']:
        return redirect(url_for('inicio', mensaje='mensaje'))

    access_token = genera_token(request.form['usuario'], request.form['contrasenia'])
    expires_in = obten_tiempo_expiracion(access_token)

    token = {'token_type': 'JWT',
            'expires_in': expires_in,
            'access_token': access_token, 
            'refresh_token': "refresh_token"}

    return redirect(url_for('inicio', token=token))
    #return jsonify({'token_type': 'JWT',
                    #'expires_in': expires_in,
                    #'access_token': access_token, 
                    #'refresh_token': "refresh_token"})


@app.route('/unprotected')
def unprotected():
    return jsonify ({'message': 'Anyone can view this!'})

@app.route('/protected')
@token_required
def protected():
    return jsonify ({'message': 'This is only available for people with valid tokens.'})

if __name__ == "__main__":
    app.run(debug=True)

    #flask --app app run --debug
    #sidesea/Scripts/activate 