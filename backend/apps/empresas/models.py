#Classes Empresa, Endereco, UsuarioEmpresa

from django.db import models

class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length=200)
    nome_fantasia = models.CharField(max_length=200, blank=True, null=True)
    cnpj = models.CharField(unique=True, max_length=18)
    representante_legal = models.ForeignKey('usuarios.Usuario', models.DO_NOTHING, db_column='representante_legal', blank=True, null=True)
    segmento = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    data_cadastro = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'


class Endereco(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey('empresas.Empresa', models.DO_NOTHING, db_column='id_empresa')
    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=150)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'endereco'


class UsuarioEmpresa(models.Model):
   #pk = models.CompositePrimaryKey('id_usuario', 'id_empresa')
    id_usuario = models.ForeignKey('usuarios.Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_empresa = models.ForeignKey('empresas.Empresa', models.DO_NOTHING, db_column='id_empresa')
    cargo = models.CharField(max_length=100, blank=True, null=True)
    status_vinculo = models.CharField(max_length=20, blank=True, null=True)
    data_vinculo = models.DateTimeField(blank=True, null=True)
    validade_permissao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_empresa'
        # Isso informa ao Django que a combinação desses dois campos é única, o que é necessário para simular uma chave primária composta
        unique_together = (('id_usuario', 'id_empresa'),)
