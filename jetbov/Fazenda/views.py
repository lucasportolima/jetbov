from django.shortcuts import render

def home(request):
	var = "creu"
	return render(request, 'base.html', {'var': var})