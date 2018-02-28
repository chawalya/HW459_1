from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django.contrib.admin import widgets
import datetime
from .models import Car,Rent,Person
class CarForm(ModelForm):
	class Meta:
		model =  Car
		exclude=[]

	def __int__(self, *args, **kwargs):
		super(CarForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))
class RentForm(ModelForm):
	class Meta:
		model =  Rent
		exclude=['user','fee','return_datetime']
	def __init__(self, *args, **kwargs):
		super(RentForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))


class PersonForm(ModelForm):
	class Meta:
		model =  Person
		exclude=[]
	def __init__(self, *args, **kwargs):
		super(PersonForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))
