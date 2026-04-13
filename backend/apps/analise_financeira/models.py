#Classe DadoFinanceiro e PeriodoContabil

from django.db import models

class DadoFinanceiro(models.Model):
    id_dado = models.AutoField(primary_key=True)
    id_documento = models.ForeignKey('documentos.Documento', models.DO_NOTHING, db_column='id_documento', blank=True, null=True)
    id_empresa = models.ForeignKey('empresas.Empresa', models.DO_NOTHING, db_column='id_empresa')
    id_periodo = models.ForeignKey('analise_financeira.PeriodoContabil', models.DO_NOTHING, db_column='id_periodo')
    id_usuario_validador = models.ForeignKey('usuarios.Usuario', models.DO_NOTHING, db_column='id_usuario_validador', blank=True, null=True)
    tipo_dado = models.CharField(max_length=50)
    categoria = models.CharField(max_length=100)
    valor_numerico = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    valor_texto = models.CharField(max_length=255, blank=True, null=True)
    score_confianca_ia = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dado_financeiro'

class PeriodoContabil(models.Model):
    id_periodo = models.AutoField(primary_key=True)
    mes_referente = models.CharField(max_length=20)
    abertura = models.DateField(blank=True, null=True)
    fechamento = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periodo_contabil'