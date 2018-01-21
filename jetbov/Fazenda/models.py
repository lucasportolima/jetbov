from django.db import models

class Fazenda(models.Model):
    """Dados de Fazenda"""

    class Meta:
        verbose_name = u'Fazenda'
        verbose_name_plural = u'Fazendas'

    cnpj = models.CharField(verbose_name=u'CNPJ', max_length=18, db_index=True, null=False, blank=False)
    nome_propriedade = models.CharField(max_length=128,
                                        verbose_name=u"Nome Fazenda",
                                        help_text=u"Nome da fazenda",
                                        null=True,
                                        blank=True)

    def __str__(self):
        return self.nome_propriedade