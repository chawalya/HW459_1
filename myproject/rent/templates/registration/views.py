from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView


from django.shortcuts import render
def home(request):
	return render(request, 'home.html', {'key': "value" })
