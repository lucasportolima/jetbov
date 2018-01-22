from rest_framework.permissions import BasePermission

class FazendaEditDeletePermission(BasePermission):
	print("sadsadas")
	message = 'Você não tem permissão para Editar/Excluir essa Fazenda.'
	def has_object_permission(self, request, view, obj):
		print(obj.proprietario.user, request.user)
		if obj.proprietario.user == request.user:
			return True
		else:
			return False
		