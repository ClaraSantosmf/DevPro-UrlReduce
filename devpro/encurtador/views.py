from django.http import HttpResponse
from django.shortcuts import render, redirect

from devpro.encurtador.models import UrlRedirect

def index(request):
    return render(request, 'index.html')

def relatorio(request, slug):
    quarysetdourldestino = UrlRedirect.objects.get(slug=slug)
    url_reduzida = request.build_absolute_uri(f'/{slug}')
    contexto  = {
        'urldestino': quarysetdourldestino,
        'url_reduzida': url_reduzida
    }
    return render(request, 'reduce.html', contexto)


def redirecionador(request, slug):
    urldestino = UrlRedirect.objects.get(slug=slug)
    return redirect(urldestino.destino)
