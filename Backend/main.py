from Manager import manager
from flask import Flask, jsonify, request
from flask.json import jsonify
from xml.etree import ElementTree as ET
from Backend.Modelos.Mensaje import Mensaje
from Backend.Modelos.Servicio import Servicio
from Backend.Modelos.Empresa import Empresa

import regex

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
    print("a")
    xml = request.get_data().decode('utf-8')
    raiz = ET.XML(xml)
    dict = raiz.find('diccionario')
    sentimientos_positivos = dict.find('sentimientos_positivos').findall('palabra')
    sp = []
    sentimientos_negativos = dict.find('sentimientos_negativos').findall('palabra')
    sn = []
    for spositivo in sentimientos_positivos:
        sp.append(spositivo)
    for snegativo in sentimientos_negativos:
        sn.append(snegativo)
    # guardo los mensajes
    lista_mensajes = raiz.find('lista_mensajes')
    mensajes = lista_mensajes.findall('mensaje')
    # lista de mensajes
    m = []
    for mensaje in mensajes:
        cad_lugarFecha = regex.search("Lugar(\s+|\t+|\n+)y(\s+|\t+|\n+)fecha:(\s+|\t+|\n+)([a-zA-Z]+),(\s+|\t+|\n+)([0-9]{2}\/[0-9]{2}\/[0-9]{4})(\s+|\t+|\n+)([0-9]{2}:[0-9]{2})",
                         mensaje.text).group(0)
        lugar = cad_lugarFecha[cad_lugarFecha.index(':'):cad_lugarFecha.index(',')]
        fecha_hora = cad_lugarFecha.split(',')[1]
        usuario = regex.search("(?<=(Usuario:(\s|\t|\n)+)).+(?=Red)",mensaje.text)
        red = regex.search("(?<=(Red(\s|\t|\n)+social:))(\s|\t|\n)+[a-zA-Z]+",mensaje.text)
        texto = regex.sub("\n*","", regex.search("(?<=Red(\s|\t|\n)+social:(\s|\t|\n)+[a-zA-Z]+(\s|\t|\n)+)(.|(\s|\t|\n))+", mensaje.text).group(0))
        # Guardo el mensaje como tal
        m.append(Mensaje(usuario, red, fecha_hora, lugar, texto))
    empresas = dict.find('empresas_analizar').findall('empresa')
    # lista de servicios
    s = []
    # lista de empresas
    emp = []
    # lista de alias
    a = []
    for empresa in empresas:
        servicios = empresa.findall('servicio')
        for serv in servicios:
            alias = serv.findall('alias')
            for al in alias:
                a.append(al.text)
            s.append(Servicio(serv.attrib['nombre'],a))
        emp.append(Empresa(empresa.find('nombre').text,s))
    mn.agregar_solicitud(m, sn, sp, emp)
    a = 1
    return jsonify({'ok': True, 'msg': 'solicitud guardada correctamente!'}), 200


if __name__=='__main__':
    app.run(debug=True, port=4000)