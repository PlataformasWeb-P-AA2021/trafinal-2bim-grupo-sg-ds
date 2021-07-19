from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return """<p> API Flask </p>
              <a href="/personas">Personas</a>
              <br>
              <a href="/barrios">Barrios</a>
              <br>
			  <a href="/casas">Casas</a>
			  <br>
			  <a href="/departamentos">Departamentos</a>
    	   """

@app.route("/personas")
def obtener_personas():
    r = requests.get("http://127.0.0.1:8000/api/personas/",
            auth=('sdgarcia6', '1'))
    personas = json.loads(r.content)
    return render_template("personas-obtenidas.html", personas=personas)

@app.route("/barrios")
def obtener_edificio():
    r = requests.get("http://127.0.0.1:8000/api/barrios/",
            auth=('sdgarcia6', '1'))
    barrios = json.loads(r.content)
    return render_template("barrios-obtenidos.html", barrios=barrios)

@app.route("/casas")
def obtener_casas():
    r = requests.get("http://127.0.0.1:8000/api/casas/",
            auth=('sdgarcia6', '1'))
    datos = json.loads(r.content)
    numero_casas = json.loads(r.content)
    casas = []
    for d in datos:
        casas.append({'propietario':obtener_nombre_persona(d['propietario']), 'direccion':d['direccion'], 'barrio': obtener_nombre_barrio(d['barrio']),
        'valorBien':d['valorBien'], 'colorInmueble':d['colorInmueble'], 'numCuartos':d['numCuartos'], 'numPisos':d['numPisos']  })
    return render_template("casas-obtenidas.html", casas=casas)

@app.route("/departamentos")
def obtener_departamentos():
    r = requests.get("http://127.0.0.1:8000/api/departamentos/",
            auth=('sdgarcia6', '1'))
    datos = json.loads(r.content)
    departamentos = []
    for d in datos:
        departamentos.append({'propietario':obtener_nombre_persona(d['propietario']), 'direccion':d['direccion'], 'barrio': obtener_nombre_barrio(d['barrio']),
        'valorBien':d['valorBien'], 'numCuartos':d['numCuartos'], 'valorMantenimiento':d['valorMantenimiento']  })
    return render_template("departamentos-obtenidos.html", departamentos=departamentos)


# Secundarios
def obtener_nombre_persona(url):
    r = requests.get(url, auth=('sdgarcia6', '1'))
    nombre_persona = json.loads(r.content)['nombre']
    return nombre_persona

def obtener_nombre_barrio(url):
    r = requests.get(url, auth=('sdgarcia6', '1'))
    nombre_barrio = json.loads(r.content)['nombre']
    return nombre_barrio

