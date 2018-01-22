from django.contrib import admin
from Fazenda.models import Fazenda, Proprietario

class FazendaAdmin(admin.ModelAdmin):
	model = Fazenda
	exclude = ('token',)
	list_display = ('cnpj','nome_propriedade', 'token')
	list_filter = ('cnpj','nome_propriedade','proprietario', 'token')
	search_fields = ('cnpj','nome_propriedade','proprietario', 'token')
	readonly_fields = ('token',)

class ProprietarioAdmin(admin.ModelAdmin):
	model = Proprietario
	exclude = ('data_cadastro',)
	list_display = ('data_cadastro',
					'nome',
					'cpf',
					'cnpj',
					'sexo',
					'nascimento',
					'naturalidade',
					'nacionalidade',
					'estado_civil',
					'profissao')
	list_filter = ('data_cadastro',
					'nome',
					'cpf',
					'cnpj',
					'sexo',
					'nascimento',
					'naturalidade',
					'nacionalidade',
					'estado_civil',
					'profissao')
	search_fields = ('data_cadastro',
					'nome',
					'cpf',
					'cnpj',
					'sexo',
					'nascimento',
					'naturalidade',
					'nacionalidade',
					'estado_civil',
					'profissao')
	readonly_fields = ('data_cadastro',)

admin.site.register(Fazenda, FazendaAdmin)
admin.site.register(Proprietario, ProprietarioAdmin)


