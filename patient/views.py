from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from .models import patientregistermodel,patientloginmodel,patientappointmentmodel
from .forms import patientregisterform,patientloginform,patientappointmentform
from django.contrib.auth import authenticate,login,logout
from hostipal.models import bloodbank,hospitalhomemodel

# Create your views here.

def patientregisterview(request):
    if request.method == 'POST':
        user = patientregistermodel.objects.filter(username=request.POST['username'])
        if user.exists():
            messages.info(request,'User already exists')
            return redirect(reverse('patient:plogin'))
        form = patientregisterform(request.POST,request.FILES)
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect(reverse("patient:plogin"))
    f=patientregisterform()
    return render(request,'patientregister.html',context={'form':f})


def patientloginview(request):
    if request.method == 'POST':
        form=patientloginform(request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
        if user:
            login(request,user)
            return redirect(reverse("phome"))
        else:
            messages.error(request,'invalidpassword')
            return redirect(reverse('patient:plogin'))
    f=patientloginform()
    return render(request,'patientlogin.html',{"form":f})

def patientlogoutview(request):
    logout(request)
    return redirect(reverse('plogin'))

def patienthomeview(request):
    return render(request,'patienthome.html')

def patienthosptialview(request):
    data=hospitalhomemodel.objects.all()
    return render(request,'patienthospital.html',{'data':data})

def patientbloodbankview(request):
    data = bloodbank.objects.all()
    return render(request,'patientbloodbank.html',context={"data":data})

def patientprofileview(request):
    if request.method =="POST":
        form=patientappointmentform(method.POST)
        if form.is_valid():
            form.save(commit=True)
    f=patientappointmentform()
    return render(request,'patientprofile.html',context={'form':f})