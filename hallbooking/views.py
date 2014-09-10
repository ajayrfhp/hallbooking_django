# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect
from hallbooking.models import Room
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
			context_dict={'Rooms':room_list,'form':form,'x':form.errors}
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
