#Classe Relatorio

from django.db import models

class Relatorio(models.Model):
    id_relatorio = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey('empresas.Empresa', models.DO_NOTHING, db_column='id_empresa')
    link_pdf = models.CharField(max_length=255)
    criacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'relatorio'