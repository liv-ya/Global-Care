from tkinter import ACTIVE
from django.db import models

from Admin.models import Place,Hospitaltype
# Create your models here.
class NewUser(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    photo=models.FileField(upload_to='images/')
    password=models.CharField(unique=True,max_length=50)        

class Hospital(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    logo=models.FileField(upload_to='logo/')
    proof=models.FileField(upload_to='proof/')
    hospitaltype=models.ForeignKey(Hospitaltype,on_delete=models.CASCADE)
    password=models.CharField(unique=True,max_length=50)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    status=models.IntegerField(default=0)

