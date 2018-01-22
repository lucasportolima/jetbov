from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	RetrieveAPIView,
	UpdateAPIView,
	DestroyAPIView,
	)

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from Fazenda.models import Fazenda, Proprietario

from .permissions import FazendaEditDeletePermission

from .serializers import (
	FazendaSerializer,
	FazendaSerializerUpdate,
	ProprietarioSerializer,
	)

class FazendaCreateAPI(CreateAPIView):
	queryset = Fazenda.objects.all()
	serializer_class = FazendaSerializerUpdate
	permission_classes = [IsAuthenticated]

class FazendaListAPI(ListAPIView):
	queryset = Fazenda.objects.all()
	serializer_class = FazendaSerializer

class FazendaDetailAPI(RetrieveAPIView):
	queryset = Fazenda.objects.all()
	serializer_class = FazendaSerializer
	lookup_field = 'token'

class FazendaDestroyAPI(DestroyAPIView):
	queryset = Fazenda.objects.all()
	serializer_class = FazendaSerializer
	lookup_field = 'token'
	permission_classes = [FazendaEditDeletePermission]

class FazendaUpdateAPI(UpdateAPIView):
	queryset = Fazenda.objects.all()
	serializer_class = FazendaSerializerUpdate
	lookup_field = 'token'
	permission_classes = [IsAuthenticatedOrReadOnly, FazendaEditDeletePermission]

class ProprietarioListAPI(ListAPIView):
	queryset = Proprietario.objects.all()
	serializer_class = ProprietarioSerializer

class ProprietarioDetailAPI(RetrieveAPIView):
	queryset = Proprietario.objects.all()
	serializer_class = ProprietarioSerializer