from django.contrib import admin
from Fazenda.models import Fazenda

class FazendaAdmin(admin.ModelAdmin):
	model = Fazenda
	# data_hierarchy = 'alguma data'
	# exclude = ('campo', 'campo')
	list_display = ('cnpj','nome_propriedade')
	list_filter = ('cnpj','nome_propriedade')
	search_fields = ('cnpj','nome_propriedade')
	# readonly_fields = campo nao editavel

admin.site.register(Fazenda, FazendaAdmin)

# Register your models here.
