from django.db.models import Count
from django.db.models.functions import TruncDate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Count
from django.urls import reverse

from devpro.encurtador.models import UrlRedirect, UrlLogs

def index(request):
    return render(request, 'index.html')

def registrado(request):
    if request.method == 'POST':
        slug = request.POST['slug']
        UrlRedirect.objects.create(
        destino=request.POST.get('destino'),
        slug=request.POST.get('slug'),
        )
        return redirect(f'/relatorio/{slug}')


def relatorio(request, slug):
    querysetdourldestino = UrlRedirect.objects.get(slug=slug)
    url_reduzida = request.build_absolute_uri(f'/{slug}')
    redirect_por_data = list(UrlRedirect.objects.filter(slug=slug).annotate(Data=TruncDate('logs__criado_em')).annotate(cliques=Count('Data')).order_by('Data'))
    for r in redirect_por_data:
        total_de_clique =+ r.cliques
    contexto  = {
        'urldestino': querysetdourldestino,
        'url_reduzida': url_reduzida,
        'redirect_por_data': redirect_por_data,
        'total_de_clique': total_de_clique
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
    if urldestino.destino.startswith('http://') or urldestino.destino.startswith('https://'):
        return redirect(urldestino.destino)
    return redirect('http://' + urldestino.destino)
