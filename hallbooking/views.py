from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect
from hallbooking.models import Room,Bookings
from hallbooking.forms import TestForm
import sys
import imaplib
session={}
def home(request):
	context = RequestContext(request)
	form=TestForm()
	if(request.method=='POST'):
		room_list=Room.objects.order_by('name')
		form=TestForm(request.POST)
		if form.is_valid():
			if 'rollnumber' not in session:
				return redirect('index')			
			x=55
			##context_dict={'Rooms':room_list,'x':x}
			##return render_to_response('hallbooking/home.html',context_dict,context)
			date_to_check=str(form['date_booking'].value())
			bookings_that_day=Bookings.objects.all().filter(date_booking=date_to_check)
			status={}
			y=True
			##my_bookings=Bookings.objects.get(rollnumber=session['rollnumber'])
			my_bookings=Bookings.objects.all().filter(rollnumber=session['rollnumber'])
			for books in bookings_that_day:
				b_end=int(books.endtime)
				b_start=int(books.starttime)
				f_start=int(form['starttime'].value())
				f_end=int(form['endtime'].value())
				if(b_end<=f_start and b_end<=f_end):
					sex='sex'
				elif(b_start>=f_start and b_start>=f_end):
					sex='sex'
				else:	
					status[str(books)]=False
					y=False
			if(y):		
				context_dict={'Rooms':room_list,'form':form,'x':status,'y':y,'my_bookings':my_bookings}
			else:
				context_dict={'Rooms':room_list,'form':form,'x':status,'my_bookings':my_bookings}

			return render_to_response('hallbooking/home.html',context_dict,context)			
		else:
			print form.errors
			context_dict={'Rooms':room_list,'form':form,'x':form.errors,'my_bookings':my_bookings}
			return render_to_response('hallbooking/home.html',context_dict,context)			

	else:
		if 'rollnumber' not in session:
			return redirect('index')
		my_bookings=Bookings.objects.all().filter(rollnumber=session['rollnumber'])
		context = RequestContext(request)
		room_list=Room.objects.order_by('name')
		form3=TestForm()
		context_dict={'Rooms':room_list,'form':form3,'my_bookings':my_bookings}
		return render_to_response('hallbooking/home.html',context_dict,context)

def login(request):
	if(request.method=='POST'):
		context = RequestContext(request)
		host='webmail.nitt.edu'
		port=143
		rollnumber=request.POST['rollnumber']
		password=request.POST['password']
		conn=imaplib.IMAP4(host)
		try:
			conn.login(rollnumber,password)
			session['rollnumber']=rollnumber
			print 'logged in '+rollnumber
			return redirect('home')
		except conn.error:
			print 'login unsuccesful'
		return redirect('index')

def logout(request):
	session.pop('rollnumber',None)
	return redirect('index')


			
		


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

	
