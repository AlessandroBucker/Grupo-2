
#Class Documento

from django.db import models

class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey('empresas.Empresa', models.DO_NOTHING, db_column='id_empresa')
    id_periodo = models.ForeignKey('analise_financeira.PeriodoContabil', models.DO_NOTHING, db_column='id_periodo')
    tipo = models.CharField(max_length=50)
    arquivo_path = models.CharField(max_length=255)
    data_upload = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documento'