from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .forms import CarForm , RentForm , PersonForm
from .models import Car,Rent,User,Person
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
class ListCarView(ListView):
    model = Car
    template_name='list.html'
class CreatePersonView(CreateView):
	queryset = Person()
	template_name='createUser.html'
	form_class = PersonForm
	success_url = '/admin'
class CreateRentView(CreateView):
    queryset = Rent()
    template_name='rent.html'
    form_class = RentForm
    success_url = '/rent'
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(CreateRentView, self).form_valid(form)
# def addRent(request):
#  model = Rent()
#  car = Car()
#  car.model = "toyata"
#  car.price = 1223
#  car.detail ="eweweqw"
#  car.save()
#  model.user= request.user
#  model.car = car
#  model.start_datetime = '2018-02-21'
#  model.stop_datetime ='2018-02-24'
#  model.fee='200'
#  model.save()
#  return render(request, 'rent.html')

#def home(request):
    # return 'Hello World'
    #print(HttpResponse('Hello'))
