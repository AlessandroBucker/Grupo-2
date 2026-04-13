# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DadoFinanceiro(models.Model):
    id_dado = models.AutoField(primary_key=True)
    id_documento = models.ForeignKey('Documento', models.DO_NOTHING, db_column='id_documento', blank=True, null=True)
    id_empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='id_empresa')
    id_periodo = models.ForeignKey('PeriodoContabil', models.DO_NOTHING, db_column='id_periodo')
    id_usuario_validador = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario_validador', blank=True, null=True)
    tipo_dado = models.CharField(max_length=50)
    categoria = models.CharField(max_length=100)
    valor_numerico = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    valor_texto = models.CharField(max_length=255, blank=True, null=True)
    score_confianca_ia = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dado_financeiro'


class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='id_empresa')
    id_periodo = models.ForeignKey('PeriodoContabil', models.DO_NOTHING, db_column='id_periodo')
    tipo = models.CharField(max_length=50)
    arquivo_path = models.CharField(max_length=255)
    data_upload = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documento'


class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length=200)
    nome_fantasia = models.CharField(max_length=200, blank=True, null=True)
    cnpj = models.CharField(unique=True, max_length=18)
    representante_legal = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='representante_legal', blank=True, null=True)
    segmento = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    data_cadastro = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'


class Endereco(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='id_empresa')
    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=150)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'endereco'


class HistoricoNotificacao(models.Model):
    id_notificacao = models.AutoField(primary_key=True)
    id_destinatario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_destinatario')
    id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)
    tipo_alerta = models.CharField(max_length=50)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(blank=True, null=True)
    recebido = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historico_notificacao'


class LogAuditoria(models.Model):
    id_log = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    acao = models.CharField(max_length=50)
    entidade_afetada = models.CharField(max_length=50)
    detalhes = models.TextField(blank=True, null=True)
    data_hora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_auditoria'


class Modulo(models.Model):
    id_modulo = models.AutoField(primary_key=True)
    nome_modulo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'modulo'


class PeriodoContabil(models.Model):
    id_periodo = models.AutoField(primary_key=True)
    mes_referente = models.CharField(max_length=20)
    abertura = models.DateField(blank=True, null=True)
    fechamento = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periodo_contabil'


class Permissoes(models.Model):
    id_permissoes = models.AutoField(primary_key=True)
    id_modulo = models.ForeignKey(Modulo, models.DO_NOTHING, db_column='id_modulo')
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_tipo_permissao = models.ForeignKey('TipoPermissao', models.DO_NOTHING, db_column='id_tipo_permissao')

    class Meta:
        managed = False
        db_table = 'permissoes'


class Relatorio(models.Model):
    id_relatorio = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='id_empresa')
    link_pdf = models.CharField(max_length=255)
    criacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'relatorio'


class TermoAceiteLgpd(models.Model):
    id_termo = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    versao = models.CharField(max_length=20)
    data_aceite = models.DateTimeField(blank=True, null=True)
    ip_usuario = models.CharField(max_length=45)
    status_consentimento = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'termo_aceite_lgpd'


class TipoPermissao(models.Model):
    id_tipo_permissao = models.AutoField(primary_key=True)
    tipo_permissao = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_permissao'


class TipoUsuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    tipo_usuario = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    email = models.CharField(unique=True, max_length=150)
    senha = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    id_tipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='id_tipo_usuario')
    cpf = models.CharField(unique=True, max_length=14, blank=True, null=True)
    crc = models.CharField(max_length=20, blank=True, null=True)
    data_cadastro = models.DateTimeField(blank=True, null=True)
    ultimo_acesso = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class UsuarioEmpresa(models.Model):
    pk = models.CompositePrimaryKey('id_usuario', 'id_empresa')
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario')
    id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='id_empresa')
    cargo = models.CharField(max_length=100, blank=True, null=True)
    status_vinculo = models.CharField(max_length=20, blank=True, null=True)
    data_vinculo = models.DateTimeField(blank=True, null=True)
    validade_permissao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_empresa'
