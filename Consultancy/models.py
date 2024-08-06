from django.db import models
from Hospital.models import Doctor
# Create your models here.
class availability(models.Model):
    date=models.DateField(max_length=50)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    from_time=models.CharField(max_length=50)
    To_time=models.CharField(max_length=50)

class Slots(models.Model):
    davaillable=models.ForeignKey(availability,on_delete=models.CASCADE)
    slotno=models.IntegerField()
    status=models.IntegerField(default=0)