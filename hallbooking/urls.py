from django.conf.urls import patterns, url
from hallbooking import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^index/', views.index, name='index'),
        url(r'^home/', views.home, name='home'),
        url(r'^check_availability/$', views.check_availability, name='check_availability'),
        url(r'^login/$', views.login, name='login'),
        url(r'^logout/$', views.logout, name='logout')
        ) 
        