from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect
from hallbooking.models import Room,Bookings
from hallbooking.forms import TestForm
def home(request):
	context = RequestContext(request)
	form=TestForm()
	if(request.method=='POST'):
		room_list=Room.objects.order_by('name')
		form=TestForm(request.POST)
		if form.is_valid():
			x=55
			##context_dict={'Rooms':room_list,'x':x}
			##return render_to_response('hallbooking/home.html',context_dict,context)
			date_to_check=str(form['date_booking'].value())
			bookings_that_day=Bookings.objects.filter(date_booking=date_to_check)
			status={}
			y=''
			for books in bookings_that_day:
				b_end=int(books.endtime)
				b_start=int(books.starttime)
				f_start=int(form['starttime'].value())
				f_end=int(form['endtime'].value())
				if(b_end<=f_start and b_end<=f_end):
					y='safe machan'
				elif(b_start>=f_start and b_start>=f_end):
					y='you are also fine'
				else:	
					status[str(books)]=False
					y=''
			context_dict={'Rooms':room_list,'form':form,'x':status,'y':y}
			return render_to_response('hallbooking/home.html',context_dict,context)			
		else:
			print form.errors
			context_dict={'Rooms':room_list,'form':form,'x':form.errors}
			return render_to_response('hallbooking/home.html',context_dict,context)			

	else:
		context = RequestContext(request)
		room_list=Room.objects.order_by('name')
		form3=TestForm()
		context_dict={'Rooms':room_list,'form':form3}
		return render_to_response('hallbooking/home.html',context_dict,context)

def index(request):
	context = RequestContext(request)
	return render_to_response('hallbooking/index.html', context)
def check_availability(request):
	context = RequestContext(request)
	blah=request.GET['data']
	return HttpResponse(blah)
