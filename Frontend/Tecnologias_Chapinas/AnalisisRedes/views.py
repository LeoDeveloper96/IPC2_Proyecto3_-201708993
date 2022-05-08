from django.shortcuts import render
from django.http import HttpResponse
import requests

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

def enviar(request):
    pass