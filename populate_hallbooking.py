import os
import time
def populate():
	r1=add_room('A12')
	r1=add_room('A13')
	r1=add_room('A2')
	r1=add_room('A11')
	r1=add_room('EEE Audi')
	r1=add_room('Civil Audi')
	r1=add_room('Barn')
	add_bookings(name=r1,rollnumber=1234,organization='Delta',time_of_booking=datetime.now(),mr=85,staff_mailid='106112003@nitt.edu',starttime=12,endtime=14,is_alloted=False)


def add_bookings(name,rollnumber,organization,time_of_booking,mr,staff_mailid,starttime,endtime,is_alloted):
	b=Bookings.objects.get_or_create(name=name,rollnumber=rollnumber,organization=organization,time_of_booking=time_of_booking,mobile_number=mr,staff_mailid=staff_mailid,starttime=starttime,endtime=endtime,is_alloted=is_alloted)[0]
	return b


def add_room(name):
	r=Room.objects.get_or_create(name=name)[0]
	return r


if __name__ == '__main__':
    print "Starting hallbooking population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
    from hallbooking.models import Bookings,Room
    populate()

