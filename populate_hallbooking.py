import os
import datetime,time
from datetime import date
def populate():
	r1=add_room('A12')
	r1=add_room('A13')
	r1=add_room('A2')
	r1=add_room('A11')
	r1=add_room('EEE Audi')
	r1=add_room('Civil Audi')
	r1=add_room('Barn')


def add_bookings(name,rollnumber,organization,mr,staff_mailid,starttime,endtime,is_alloted):
	b=Bookings.objects.get_or_create(name=name,rollnumber=rollnumber,organization=organization,mobile_number=mr,staff_mailid=staff_mailid,starttime=starttime,endtime=endtime,is_alloted=is_alloted)[0]
	return b


def add_room(name):
	r=Room.objects.get_or_create(name=name)[0]
	return r


if __name__ == '__main__':
    print "Starting hallbooking population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
    from hallbooking.models import Bookings,Room
    populate()

