from django.db import models
from Consultancy.models import Slots
from Guest.models import NewUser
# Create your models here.
class Appointment(models.Model):
    slot=models.ForeignKey(Slots,on_delete=models.CASCADE)
    appointment_date=models.DateField(max_length=50)
    appointment_status=models.IntegerField(default=0)
    user=models.ForeignKey(NewUser,on_delete=models.CASCADE)
    