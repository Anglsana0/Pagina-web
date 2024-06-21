from flask import Flask
import random

app = Flask(__name__)

lista_datos = [
    "Redes Sociales horizontales: son el tipo de redes sociales generales, donde cualquier tipo de usuario puede entrar y participar de ellas, sin tener a priori características comunes. Son, por ejemplo, Facebook, Instagram o Twitter.",
    "Redes Sociales verticales: aquí es algo diferente. Los usuarios buscan o tienen puntos en común, y estas redes sociales sirven para una o varias finalidades concretas a nivel profesional: empleo, networking, viajes, etc. Aquí entran el tipo de redes sociales como LinkedIn, Tripadvisor, Soundcloud, Spotify, Vimeo, etc…"
]

@app.route("/")
def inicio():
    return '<h1>Hola, aquí puedes ver cuáles son las redes verticales y horizontales</h1><a href="/dato_aleatorio">¡Ver un dato aleatorio!</a><br><a href="/generar_contrasena">¡Generar una contraseña!</a>'

@app.route("/dato_aleatorio")
def dato_aleatorio():
    return f'<p>{random.choice(lista_datos)}</p><a href="/">Atrás</a>'

@app.route("/generar_contrasena")
def generar_contrasena():
    longitud = 12
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return f'<p>Tu contraseña generada es: {contrasena}</p><a href="/">Atrás</a>'









app.run(debug=True)