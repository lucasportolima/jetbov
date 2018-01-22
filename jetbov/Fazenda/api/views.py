from rest_framework.generics import ListAPIView

from Fazenda.models import Fazenda, Proprietario
from .serializers import FazendaSerializer, ProprietarioSerializer

class FazendaListAPI(ListAPIView):
	queryset = Fazenda.objects.all()
	serializer_class = FazendaSerializer

class ProprietarioListAPI(ListAPIView):
	queryset = Proprietario.objects.all()
	serializer_class = ProprietarioSerializer