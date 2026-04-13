from django.db import models

class Endereco(models.Model):
    id_empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    cep = models.CharField(max_length=8)
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

class Empresa(models.Model):
    cnpj = models.CharField(max_length=18, unique=True)
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255)
    representante_legal = models.ForeignKey('usuarios.Usuario', on_delete=models.SET_NULL, null=True)
    segmento = models.CharField(max_length=100)
    status = models.CharField(max_length=20)  # Ativa, Inativa, Suspensa
    data_cadastro = models.DateTimeField(auto_now_add=True)