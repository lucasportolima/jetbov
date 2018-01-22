from django.contrib import admin
from Animal.models import Animal

class AnimalAdmin(admin.ModelAdmin):
	model = Animal
	exclude = ('data_cadastro',)
	list_display = ('codigo', 'data_cadastro', 'peso', 'idade', 'sexo', 'descricao')
	list_filter = ('codigo', 'data_cadastro', 'peso', 'idade', 'sexo', 'descricao', 'fazenda')
	search_fields = ('codigo', 'data_cadastro', 'peso', 'idade', 'sexo', 'descricao', 'fazenda')
	readonly_fields = ('data_cadastro',)

admin.site.register(Animal, AnimalAdmin)
