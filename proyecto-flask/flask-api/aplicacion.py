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
    r = requests.get("http://127.0.0.1:8000/api/personas/")
    personas = json.loads(r.content)['results']
    numero_personas = json.loads(r.content)['count']
    return render_template("personas-obtenidas.html", personas=personas,
    numero_personas=numero_personas)

@app.route("/barrios")
def obtener_edificio():
    r = requests.get("http://127.0.0.1:8000/api/barrios/",
            auth=('sdgarcia6', '1'))
    barrios = json.loads(r.content)['results']
    numero_barrios = json.loads(r.content)['count']
    return render_template("barrios-obtenidos.html", barrios=barrios,
    numero_barrios=numero_barrios)

@app.route("/casas")
def obtener_casas():
    r = requests.get("http://127.0.0.1:8000/api/casas/",
            auth=('sdgarcia6', '1'))
    datos = json.loads(r.content)['results']
    numero_casas = json.loads(r.content)['count']
    casas = []
    for d in datos:
        casas.append({'propietario':obtener_nombre_persona(d['propietario']), 'direccion':d['direccion'], 'barrio': obtener_nombre_barrio(d['barrio']),
        'valorBien':d['valorBien'], 'colorMueble':d['colorMueble'], 'numCuartos':d['numCuartos'], 'numPisos':d['numPisos']  })
    return render_template("casas-obtenidas.html", casas=casas,
    numero_casas=numero_casas)

@app.route("/departamentos")
def obtener_departamentos():
    r = requests.get("http://127.0.0.1:8000/api/departamentos/",
            auth=('sdgarcia6', '1'))
    datos = json.loads(r.content)['results']
    numero_departamentos = json.loads(r.content)['count']
    departamentos = []
    for d in datos:
        departamentos.append({'propietario':obtener_nombre_persona(d['propietario']), 'direccion':d['direccion'], 'barrio': obtener_nombre_barrio(d['barrio']),
        'valorBien':d['valorBien'], 'numCuartos':d['numCuartos'], 'valorMensual':d['valorMensual']  })

    return render_template("departamentos-obtenidos.html", departamentos=departamentos,
    numero_departamentos=numero_departamentos)


# Secundarios
def obtener_nombre_persona(url):
    r = requests.get(url, auth=('sdgarcia6', '1'))
    nombre_persona = json.loads(r.content)['nombre']
    return nombre_persona

def obtener_nombre_barrio(url):
    r = requests.get(url, auth=('sdgarcia6', '1'))
    nombre_barrio = json.loads(r.content)['nombre']
    return nombre_barrio

