

from Manager import manager
from flask import Flask, jsonify, request
from flask.json import jsonify
from xml.etree import ElementTree as ET
import re

app = Flask(__name__)


mn = manager()

# get
# Codigo de prueba
@app.route('/')
def index():
    return 'Hola, soy una API', 200

# Envia la solicitud de clasificacion
@app.route('/enviar', methods=['POST'])
def enviar():
    xml = request.get_data().decode('utf-8')
    raiz = ET.XML(xml)
    sentimientos_positivos = raiz.find('sentimientos_positivos')
    sp = []
    sentimientos_negativos = raiz.find('sentimientos_negativos')
    sn = []
    lista_mensajes = raiz.find('lista_mensajes')
    mensajes = lista_mensajes.findall('mensaje')
    mn = []
    for mensaje in mensajes:
        cad_lugarFecha = re.search("Lugar(\s+|\t+|\n+)y(\s+|\t+|\n+)fecha:(\s+|\t+|\n+)([a-zA-Z]+),(\s+|\t+|\n+)([0-9]{2}\/[0-9]{2}\/[0-9]{4})(\s+|\t+|\n+)([0-9]{2}:[0-9]{2})",
                         mensaje.text).group(0)
        lugar = cad_lugarFecha[cad_lugarFecha.index(':'):len(mensaje.text.split(',')[0])-1]
        fecha_hora = cad_lugarFecha.split(',')[1]
        usuario = re.search("Usuario:(\s|\t|\n)+[a-zA-Z0-9]+@[a-zA-Z]+.[a-zA-Z]+", mensaje.text).group(0)
        usr = usuario[usuario.index(':'):]
        red = re.search("Red(\s|\t|\n)+social:(\s|\t|\n)+[a-zA-Z]+", mensaje.text).group(0)
        red = red[red.index(':'):]
        texto = re.search("(?<=Red(\s|\t|\n)+social:(\s|\t|\n)+[a-zA-Z]+(\s|\t|\n)+)(.|(\s|\t|\n))+", mensaje.text).group(0)
        mn.append(usr,red,fecha_hora,lugar,texto)
    empresas_analizar = raiz.find('empresas_analizar')
    empresas = empresas_analizar.findall('empresa')
    s = []
    emp = []
    a = []
    for empresa in empresas:
        servicios = empresa.findall('servicio')
        for serv in servicios:
            alias = serv.findall('alias')
            for al in alias:
                a.append(al.text)
            s.append(serv.attrib['nombre'])
        emp.append(empresa.find('nombre').text)
    mn.agregar_solicitud(mn, sn, sp, emp)
    a = 1
    return jsonify({'ok': True, 'msg': 'solicitud guardada correctamente!'}), 200

# Recibe la clasificacion
@app.route('/recibir')
def recibir():
    return 'Hola, soy una API', 200

if __name__=='__main__':
    app.run(debug=True, port=4000)