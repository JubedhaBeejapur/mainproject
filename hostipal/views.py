from django.shortcuts import render
from .models import hospitalregistermodel,bloodbank,hospitalhomemodel
from.forms import hospitalregisterform
from patient.models import patientappointmentmodel
# Create your views here.

def hospitalregisterview(request):
    if request.method == 'POST':
        user = hospitalregistermodel.objects.filter(username=request.POST['username'])
        if user.exists():
            messages.info(request,'User already exists')
            return redirect(reverse('patient:plogin'))
        form = hospitalregisterform(request.POST,request.FILES)
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect(reverse("hhome"))
    f=hospitalregisterform()
    return render(request,'hospregister.html',context={'form':f})


def hbloodbankview(request):
    data= bloodbank.objects.all()
    return render(request,'hbloodbank.html',context={'data':data})

def hhomeview(request):
    data=hospitalhomemodel.objects.all()
    return render(request,'hospitalhome.html',context={"data":data})


def happointmentview(request):
    data=patientappointmentmodel.objects.all()
    return render(request,'happointmentlist.html',context={"data":data})
