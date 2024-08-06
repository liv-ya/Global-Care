from django.db import models
from Admin.models import *
from Guest.models import Hospital
# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    hospital=models.ForeignKey(Hospital,on_delete=models.CASCADE)
    photo=models.FileField(upload_to='images/')
    proof=models.FileField(upload_to='images/')
    email=models.CharField(max_length=50)
    password=models.CharField(unique=True,max_length=50) 
    status=models.IntegerField(default=0) 
    doj=models.DateField(auto_now=True) 

class Consultancy(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    headname=models.CharField(max_length=50)
    password=models.CharField(unique=True,max_length=50) 
    hospital_id=models.ForeignKey(Hospital,on_delete=models.CASCADE)

    

