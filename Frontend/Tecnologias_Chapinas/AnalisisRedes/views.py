from django.shortcuts import render
from django.http import HttpResponse
import requests
from Frontend.Tecnologias_Chapinas.AnalisisRedes.Forms import FileForm
from django.views.decorators.csrf import csrf_exempt

# una vista asociada a html se llama template en django
# una vista es un handler de peticiones en django
endpoint = 'http://127.0.0.1:4000/'


def index(request):
    # Create your views here.
    # request ->response
    # request handler
    # action
    # mapeo esta vista a una url para que cuando reciba un request a esa url se llame a esta funcion
    # return HttpResponse('Hello world')
    return render(request, 'index.html')


# 2. Eximir la vista de los chequeos de CSRF
@csrf_exempt
def enviar(request):
    ctx = {
        'response': None
    }
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            xml_binary = file.read()
            xml = xml_binary.decode('utf-8')
            response = requests.post(endpoint + 'enviar', data=xml_binary)
            if response.ok:
                ctx['response'] = response.status_code
            else:
                ctx['response'] = 'El archivo se envio, pero hubo un error en el servidor'
    else:
        print("Renderizando solo la plantilla", request.method)

    return render(request, 'index.html')
