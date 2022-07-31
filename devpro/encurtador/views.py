from django.http import HttpResponse
from django.shortcuts import render, redirect

from devpro.encurtador.models import UrlRedirect, UrlLogs

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
    logs = UrlLogs.objects.create(
        origem=request.META.get('HTTP_REFERER'),
        user_agent=request.META.get('HTTP_USER_AGENT'),
        host=request.META.get('HTTP_HOST'),
        ip=request.META.get('REMOTE_ADDR'),
        url_redirect=urldestino
    )
    return redirect(urldestino.destino)