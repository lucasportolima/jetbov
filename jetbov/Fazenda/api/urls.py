from django.urls import path
from .views import FazendaListAPI 

urlpatterns = [
	path('', FazendaListAPI.as_view(), name='list'),
]
