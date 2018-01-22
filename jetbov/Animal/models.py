import datetime

from django.db import models
from Fazenda.models import Fazenda

SEXO_MACHO = 'm'
SEXO_FEMEA = 'f'
SEXO_CHOICES = (
    (SEXO_MACHO, u'Macho'),
    (SEXO_FEMEA, u'Fêmea'),
)

class Animal(models.Model):
    """Dados de Animal"""

    class Meta:
        verbose_name = u'Animal'
        verbose_name_plural = u'Animais'

    codigo = models.CharField(verbose_name=u'Código/Brinco do Animal', unique=True, max_length=18, db_index=True, null=False, blank=False)
    data_cadastro = models.DateField(verbose_name=u'Cadastro', default=datetime.date.today, )
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, )
    idade = models.FloatField(null=True, blank=True, default=None, )
    sexo = models.CharField(verbose_name=u'Sexo', max_length=1, choices=SEXO_CHOICES, default=SEXO_MACHO, )
    descricao = models.CharField(verbose_name=u'Tipo ou Raça', max_length=100, )
    fazenda = models.ManyToManyField(Fazenda)

    def __str__(self):
        return u'Código: %s - Fazenda: %s' % (self.codigo, self.fazenda)
