from django.db import models

class Documento(models.Model):
    #Não foi criado id_documento porque o Django já cria um campo id automaticamente como chave primária
    id_empresa = models.ForeignKey('empresas.Empresa', on_delete=models.CASCADE)
    id_periodo = models.ForeignKey('analise_financeira.PeriodoContabil', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)  # Balanço, Balancete, DRE
    arquivo_path = models.CharField(max_length=500)
    data_upload = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50)  # Pendente, Enviado, Aguardando revisão, Erro