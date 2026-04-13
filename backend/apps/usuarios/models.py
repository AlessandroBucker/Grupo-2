#Classes Usuario, TipoUsuario, TermoAceiteLgpd, LogAuditoria

from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    email = models.CharField(unique=True, max_length=150)
    senha = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    id_tipo_usuario = models.ForeignKey('usuarios.TipoUsuario', models.DO_NOTHING, db_column='id_tipo_usuario')
    cpf = models.CharField(unique=True, max_length=14, blank=True, null=True)
    crc = models.CharField(max_length=20, blank=True, null=True)
    data_cadastro = models.DateTimeField(blank=True, null=True)
    ultimo_acesso = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class TipoUsuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    tipo_usuario = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class TermoAceiteLgpd(models.Model):
    id_termo = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('usuarios.Usuario', models.DO_NOTHING, db_column='id_usuario')
    versao = models.CharField(max_length=20)
    data_aceite = models.DateTimeField(blank=True, null=True)
    ip_usuario = models.CharField(max_length=45)
    status_consentimento = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'termo_aceite_lgpd'


class LogAuditoria(models.Model):
    id_log = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('usuarios.Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    acao = models.CharField(max_length=50)
    entidade_afetada = models.CharField(max_length=50)
    detalhes = models.TextField(blank=True, null=True)
    data_hora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_auditoria'