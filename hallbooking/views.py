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
	rollnumber=request.GET['rollnumber']
	name=request.GET['name']
	need_lcd=request.GET['need_lcd']
	need_audio=request.GET['need_audio']
	mobile_number=request.GET['mobile_number']
	staff_mailid=request.GET['staff_mailid']
	starttime=request.GET['starttime']
	endtime=request.GET['endtime']
	date_booking=request.GET['date_booking']
	organization=request.GET['organization']
	if(need_lcd==2):
		need_lcd=True
	else:
		need_lcd=False

	if(need_audio==2):
		need_audio=True
	else:
		need_audio=False	

	bookings_that_day=Bookings.objects.filter(date_booking=date_booking)
	status={}
	y=True
	for books in bookings_that_day:
		b_end=int(books.endtime)
		b_start=int(books.starttime)
		f_start=int(starttime)
		f_end=int(endtime)
		
		if(b_end<=f_start and b_end<=f_end):
			#add a booking
			y1=True
			##temp_room=Rooms.objects.filter(name=name)
			##k=Bookings.objects.get_or_create(name=temp_room,rollnumber=rollnumber,need_lcd=need_lcd,need_audio=need_audio,date_booking=date_booking,starttime=starttime,endtime=endtime,organization=organization,staff_mailid=staff_mailid)[0]
		elif(b_start>=f_start and b_start>=f_end):
			#add a booking
			y1=True
			##k=Bookings.objects.get_or_create(name=temp_room,rollnumber=rollnumber,need_lcd=need_lcd,need_audio=need_audio,date_booking=date_booking,starttime=starttime,endtime=endtime,organization=organization,staff_mailid=staff_mailid)[0]
		else:	
			y=False

	if(y==True):
		temp_room=Room.objects.get(name=str(name))
		k=Bookings.objects.get_or_create(name=temp_room,rollnumber=rollnumber,need_lcd=need_lcd,need_audio=need_audio,date_booking=date_booking,starttime=starttime,endtime=endtime,organization=organization,staff_mailid=staff_mailid,mobile_number=mobile_number)[0]
		y=temp_room		
	return HttpResponse(y)

	
