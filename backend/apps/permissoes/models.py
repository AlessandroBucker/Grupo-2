#Classes Permissoes, TipoPermissao, Modulo

from django.db import models

class Permissoes(models.Model):
    id_permissoes = models.AutoField(primary_key=True)
    id_modulo = models.ForeignKey('permissoes.Modulo', models.DO_NOTHING, db_column='id_modulo')
    id_usuario = models.ForeignKey('usuarios.Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_tipo_permissao = models.ForeignKey('permissoes.TipoPermissao', models.DO_NOTHING, db_column='id_tipo_permissao')

    class Meta:
        managed = False
        db_table = 'permissoes'

class TipoPermissao(models.Model):
    id_tipo_permissao = models.AutoField(primary_key=True)
    tipo_permissao = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_permissao'

class Modulo(models.Model):
    id_modulo = models.AutoField(primary_key=True)
    nome_modulo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'modulo'