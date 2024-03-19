from django.urls import path
from .import views

urlpatterns = [
    path('hregister',views.hospitalregisterview,name='hregister'),
    path("hblood/",views.hbloodbankview,name='hblood'),
    path("hhome/",views.hhomeview,name='hhome'),
    path('happointment/',views.happointmentview,name='happointment')
]
