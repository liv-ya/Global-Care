from django.db import models

# Create your models here.
class Department(models.Model):
    department_name=models.CharField(max_length=50)

    def __str__(self):
        return self.department_name

class District(models.Model):
    district_name=models.CharField(max_length=50)

    def __str__(self):
        return self.district_name

class Complainttype(models.Model):
    complaint_type=models.CharField(max_length=50)

    def __str__(self):
        return self.complaint_type

class Hospitaltype(models.Model):
    hospital_type=models.CharField(max_length=50)

    def __str__(self):
        return self.hospital_type

class Place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(District,on_delete=models.CASCADE)

    def __str__(self):
        return self.place_name

class Adminlogin(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=50)

class complaint(models.Model):
    content=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    status=models.IntegerField(default=0)
    user=models.IntegerField(default=0)
    doctor=models.IntegerField(default=0)
    hospital=models.IntegerField(default=0)
    typeid=models.ForeignKey(Complainttype,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    reply=models.CharField(max_length=50,default="Not Yet Viewed")

class feedback(models.Model):
    content=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    user=models.IntegerField(default=0)
    doctor=models.IntegerField(default=0)
    hospital=models.IntegerField(default=0)

