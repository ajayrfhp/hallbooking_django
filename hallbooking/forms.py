from django import forms
from django.forms import widgets
from  hallbooking.models import Room,Bookings,Test
import datetime 	

class BookingsForm(forms.ModelForm):
	name=forms.CharField(widget=forms.HiddenInput())
	rollnumber=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'rollnumber'}))
	organization=forms.CharField(max_length=128,widget=forms.TextInput(attrs={'placeholder': 'organization'}))
	need_lcd=forms.NullBooleanField(help_text="Need Lcd             ? ")
	need_audio=forms.NullBooleanField(help_text="Need Audio         ?  								 ")
	mobile_number=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Mobilenumber'}))
	staff_mailid=forms.CharField(max_length=128,widget=forms.TextInput(attrs={'placeholder': 'emailid of staff coordinator'}))
	starttime=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'starttime in Railwaytime'}))
	endtime=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'endtime in Railwaytime'}))
	time_of_booking=forms.DateTimeField(widget=forms.HiddenInput())
	date_booking=forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
	is_alloted=forms.NullBooleanField(widget=forms.HiddenInput())

	class Meta:
		model=Bookings
class TestForm(forms.ModelForm):
	rollnumber=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'rollnumber'}))
	organization=forms.CharField(max_length=128,widget=forms.TextInput(attrs={'placeholder': 'organization'}))
	need_lcd=forms.NullBooleanField(help_text="Need Lcd             ? ")
	need_audio=forms.NullBooleanField(help_text="Need Audio         ?  								 ")
	mobile_number=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Mobilenumber'}))
	staff_mailid=forms.CharField(max_length=128,widget=forms.TextInput(attrs={'placeholder': 'emailid of staff coordinator'}))
	starttime=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'starttime in Railwaytime'}))
	endtime=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'endtime in Railwaytime'}))
	date_booking=forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
	is_alloted=forms.NullBooleanField(widget=forms.HiddenInput())

	class Meta:
		model=Test
