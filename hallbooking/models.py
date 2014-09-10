from django.db import models
from django.utils import timezone

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
	time_of_booking=models.DateTimeField(auto_now=True)
	starttime=models.IntegerField()
	endtime=models.IntegerField()
	date_booking=models.DateField()	
	is_alloted=models.NullBooleanField(default=False)
	def __unicode__(self):
		return str(self.name)

class Test(models.Model):
	name=models.ForeignKey(Room)
	rollnumber=models.IntegerField()
	organization=models.CharField(max_length=128,null=True)
	need_lcd=models.NullBooleanField(default=False)
	need_audio=models.NullBooleanField(default=False)
	mobile_number=models.IntegerField()
	staff_mailid=models.CharField(max_length=128)
	starttime=models.IntegerField()
	endtime=models.IntegerField()
	date_booking=models.DateField()	
	is_alloted=models.NullBooleanField(default=False)
	def __unicode__(self):
		return str(self.name)


# Create your models here.