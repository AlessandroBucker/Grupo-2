from django.db import models

class HistoricoNotificacao(models.Model):
    id_notificacao = models.AutoField(primary_key=True)
    id_destinatario = models.ForeignKey('usuarios.Usuario', models.DO_NOTHING, db_column='id_destinatario')
    id_empresa = models.ForeignKey('empresas.Empresa', models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)
    tipo_alerta = models.CharField(max_length=50)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(blank=True, null=True)
    recebido = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historico_notificacao'