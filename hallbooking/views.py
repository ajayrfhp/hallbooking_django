# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from hallbooking.models import Room
from hallbooking.forms import BookingsForm
def home(request):
	context = RequestContext(request)
	room_list=Room.objects.order_by('name')
	form3=BookingsForm()
	context_dict={'Rooms':room_list,'form':form3}
	return render_to_response('hallbooking/home.html',context_dict,context)

def index(request):
	context = RequestContext(request)
	return render_to_response('hallbooking/index.html', context)
    