from django.db import models
# Create your models here.

class UrlRedirect(models.Model):
    destino = models.URLField(max_length=180)
    slug = models.SlugField(max_length= 120)
    criado_em = models.DateTimeField(auto_now_add= True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'UrlRedirect para {self.destino}'