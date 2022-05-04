

from Manager import manager
from flask import Flask, jsonify, request
from flask.json import jsonify
from xml.etree import ElementTree as ET

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
    for elemento in raiz:

        # mn.agregar_solicitud()
        pass
    return jsonify({'ok': True, 'msg': 'solicitud guardada correctamente!'}), 200

# Recibe la clasificacion
@app.route('/recibir')
def recibir():
    return 'Hola, soy una API', 200

if __name__=='__main__':
    app.run(debug=True, port=4000)