from django.db import models
from django.utils import timezone
import time
class Room(models.Model):
	name=models.CharField(max_length=128,unique=True)
	is_available=models.BooleanField(default=True)
	def __unicode__(self):
		return self.name


class Bookings(models.Model):
	name=models.ForeignKey(Room)
	rollnumber=models.IntegerField()
	organization=models.CharField(max_length=128,null=True)
	need_lcd=models.NullBooleanField(default=False)
	need_audio=models.NullBooleanField(default=False)
	mobile_number=models.IntegerField()
	staff_mailid=models.CharField(max_length=128)
	time_of_booking=models.DateTimeField(default=time.strftime("%c"))
	starttime=models.IntegerField()
	endtime=models.IntegerField()
	date=models.DateField(default=time.strftime("%d/%m/%Y"))	
	is_alloted=models.NullBooleanField(default=False)
	def __unicode__(self):
		return str(self.name)



# Create your models here.