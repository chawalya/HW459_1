from django.db import models
from django.contrib.auth.models import User
# Create your models here.
'''
	Firstname
	lastname
	telephone
	date of birth
	credit amount
	profiles image
	Memo 500 characters
'''

class Car(models.Model):
    model =models.CharField(max_length = 20)
    detail=models.CharField(max_length = 100)
    price =models.DecimalField(max_digits=10,decimal_places=2)
#    def __str__(self):
    #    return u"%s"%(self.model)
    def __str__(self):
      return u"Brand : %s - Year : %s - Fee : %d Bath"%(self.model, self.detail , self.price)

class Rent (models.Model):
    user= models.ForeignKey(User,on_delete =models.CASCADE)
    car =models.ForeignKey(Car,on_delete= models.CASCADE)
    start_datetime=models.DateTimeField(null=True)
    return_datetime=models.DateTimeField(null=True)
    fee=models.DecimalField(max_digits=10,decimal_places=2,null=True)

class Person(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	telephone=models.CharField(max_length=15)
	dob=models.DateField(blank=True,null=True)
	credit_amount=models.DecimalField(max_digits=15, decimal_places=2)
	memo=models.CharField(max_length=500)
