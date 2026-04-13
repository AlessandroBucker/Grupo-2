from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    crc = models.CharField(max_length=20, blank=True, null=True)
    perfil_acesso = models.CharField(max_length=20)  # ADM, ANALISTA, CONTADOR
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ultimo_acesso = models.DateTimeField(auto_now=True)

class TermoLGPD(models.Model):
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    versao = models.CharField(max_length=10)
    data_aceite = models.DateTimeField(null=True, blank=True)
    ip_usuario = models.CharField(max_length=50)
    status_consentimento = models.CharField(max_length=20)  # Aceito, Pendente

class UsuarioEmpresa(models.Model):
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    id_empresa = models.ForeignKey('empresas.Empresa', on_delete=models.CASCADE)
    cargo = models.CharField(max_length=50)
    permissao = models.CharField(max_length=50)
    status_vinculo = models.CharField(max_length=20)  # Ativo, Inativo, Suspenso
    data_vinculo = models.DateField()
    validade_permissao = models.DateField(null=True, blank=True)
    data_alerta = models.DateTimeField(null=True, blank=True)

class HistoricoNotificacao(models.Model):
    id_destinatario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    id_empresa = models.ForeignKey('empresas.Empresa', on_delete=models.CASCADE)
    tipo_alerta = models.CharField(max_length=50)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    recebido = models.BooleanField(default=False)