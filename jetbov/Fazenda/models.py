import datetime

from django.db import models

SEXO_MASCULINO = 'm'
SEXO_FEMININO = 'f'
SEXO_CHOICES = (
    (SEXO_MASCULINO, u'Masculino'),
    (SEXO_FEMININO, u'Feminino'),
)


ESTADOCIVIL_CASADO = 'c'
ESTADOCIVIL_SOLTEIRO = 's'
ESTADOCIVIL_DIVORCIADO = 'd'
ESTADOCIVIL_VIUVO = 'v'
ESTADOCIVIL_CHOICES = (
    (ESTADOCIVIL_CASADO, u'Casado'),
    (ESTADOCIVIL_SOLTEIRO, u'Solteiro'),
    (ESTADOCIVIL_DIVORCIADO, u'Divorciado'),
    (ESTADOCIVIL_VIUVO, u'Viúvo'),
)


class Proprietario(models.Model):
    u"""Armazena dados de Proprietario"""

    class Meta:
        verbose_name = u'Proprietario'
        verbose_name_plural = u'Proprietarios'

    data_cadastro = models.DateField(verbose_name=u'Cadastro', default=datetime.date.today, )

    nome = models.CharField(verbose_name=u'Nome', max_length=250, )

    cpf = models.CharField(verbose_name=u'CPF', max_length=14, db_index=True, null=True, blank=True)

    cnpj = models.CharField(verbose_name=u'CNPJ', max_length=18, db_index=True, null=True, blank=True)

    sexo = models.CharField(verbose_name=u'Sexo', max_length=1, choices=SEXO_CHOICES, default=SEXO_MASCULINO, )

    nascimento = models.DateField(verbose_name=u'Nascimento', null=True, blank=True)

    naturalidade = models.CharField(verbose_name=u'Naturalidade',
                                    max_length=30,
                                    blank=True,
                                    null=True)

    nacionalidade = models.CharField(verbose_name=u'Nacionalidade',
                                     max_length=30,
                                     blank=True,
                                     null=True)

    estado_civil = models.CharField(verbose_name=u'Estado Civil',
                                    max_length=1,
                                    choices=ESTADOCIVIL_CHOICES,
                                    blank=True,
                                    null=True)

    profissao = models.CharField(verbose_name=u'Profissão',
                                 max_length=50,
                                 blank=True,
                                 null=True)

    def __str__(self):
        if self.cpf and self.cnpj:
            return u'Nome: %s - CPF: %s - CNPJ: %s' % (self.nome, self.cpf, self.cnpj)
        elif self.cpf:
            return u'Nome: %s - CPF: %s' % (self.nome, self.cpf)
        else:
            return u'Nome: %s - CNPJ: %s' % (self.nome, self.cnpj)


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
    proprietario = models.ManyToManyField(Proprietario, verbose_name=u'Proprietários',
                                          blank=True, null=True, )

    def __str__(self):
        return self.nome_propriedade
