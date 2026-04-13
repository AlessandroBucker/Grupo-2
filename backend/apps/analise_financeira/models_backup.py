from django.db import models

#Não foi criado id_periodo nem id_dado porque o Django já cria um campo id automaticamente como chave primária

class PeriodoContabil(models.Model):
    mes_referente = models.IntegerField()
    abertura = models.DateField()
    fechamento = models.DateField()
    status = models.CharField(max_length=20)  # Aberto, Fechado, EmRevisão

class DadoFinanceiro(models.Model):
    id_documento = models.ForeignKey('documentos.Documento', on_delete=models.CASCADE)
    id_usuario_validador = models.ForeignKey('usuarios.Usuario', on_delete=models.SET_NULL, null=True, blank=True)
    tipo_dado = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    valor_numerico = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    valor_texto = models.TextField(null=True, blank=True)
    score_confianca_ia = models.FloatField(null=True, blank=True)