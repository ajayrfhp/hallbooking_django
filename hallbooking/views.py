# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect
from hallbooking.models import Room
from hallbooking.forms import BookingsForm

def home(request):
	if( not request.GET.has_key('q')):
		context = RequestContext(request)
		room_list=Room.objects.order_by('name')
		form3=BookingsForm()
		context_dict={'Rooms':room_list,'form':form3}
	else:
		context = RequestContext(request)
		room_list=Room.objects.order_by('name')
		form3=request.GET['q']
		context_dict={'Rooms':room_list,'form':form3}

	return render_to_response('hallbooking/home.html',context_dict,context)

def index(request):
	context = RequestContext(request)
	return render_to_response('hallbooking/index.html', context)
def check_availability(request):
	context = RequestContext(request)
	form=BookingsForm()
	if(request.method=='GET'):
		room_list=Room.objects.order_by('name')
		form=BookingsForm(request.GET)
		if form.is_valid():
			x=5
		else:
			print form.errors
			context_dict={'Rooms':room_list,'form':form}
			return redirect('/hallbooking/home/?q='+str(form)) 		
	else:
		room_list=Room.objects.order_by('name')
		form=BookingsForm(request.GET)
		context_dict={'Rooms':room_list,'form':form}

		return render_to_response('hallbooking/home.html',context_dict,context)		

	context_dict={'Rooms':room_list,'form':form}			
	return render_to_response('hallbooking/home.html',context_dict,context)



    