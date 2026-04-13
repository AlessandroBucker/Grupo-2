from django.db import models

class Relatorio(models.Model):
    id_empresa = models.ForeignKey('empresas.Empresa', on_delete=models.CASCADE)
    link_pdf = models.CharField(max_length=500)
    criacao = models.DateTimeField(auto_now_add=True)