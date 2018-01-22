from rest_framework.serializers import ModelSerializer

from Fazenda.models import Fazenda, Proprietario

class FazendaSerializer(ModelSerializer):
	class Meta:
		model = Fazenda
		fields = [
			'cnpj',
			'token',
			'nome_propriedade',
			'proprietario',
		]

class FazendaSerializerUpdate(ModelSerializer):
	class Meta:
		model = Fazenda
		fields = [
			'cnpj',
			'nome_propriedade',
			'proprietario',
		]


class ProprietarioSerializer(ModelSerializer):
	class Meta:
		model = Proprietario
		fields = [
			'user',
			'data_cadastro',
			'nome',
			'cpf',
			'cnpj',
			'sexo',
			'nascimento',
			'naturalidade',
			'nacionalidade',
			'estado_civil',
			'profissao',
		]