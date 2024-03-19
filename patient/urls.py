from django.urls import path
from . import views

urlpatterns = [
    path('pregister/',views.patientregisterview,name='pregister'),
    path("plogin/",views.patientloginview,name='plogin'),
    path('phome/',views.patienthomeview,name='phome'),
    path('phospatial/',views.patienthosptialview,name='phospital'),
    path('pbloodbank/',views.patientbloodbankview,name='pbloodbank'),
    path('pprofile',views.patientprofileview,name='pprofile')
]
