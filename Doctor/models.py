from django.db import models
from User.models import Appointment
# Create your models here.
class Prescribtion(models.Model):
    medicine_details=models.CharField(max_length=100)
    diet=models.CharField(max_length=50,null=True)
    appointment=models.ForeignKey(Appointment,on_delete=models.CASCADE)

class MedicineReport(models.Model):
    report_file=models.FileField(upload_to='images/')
    report_details=models.CharField(max_length=100)
    major=models.CharField(max_length=50)
    appointment=models.ForeignKey(Appointment,on_delete=models.CASCADE)