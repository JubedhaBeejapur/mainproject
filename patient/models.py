from django.db import models

# Create your models here.

class patientregistermodel(models.Model):
    name=models.CharField(max_length=35)
    age=models.IntegerField()
    phone_no=models.CharField(max_length=12)
    gender=models.CharField(max_length=6)
    blood_grp = models.CharField(max_length=5)
    height=models.DecimalField(decimal_places=5,max_digits=10)
    weight=models.IntegerField()
    material_status=models.CharField(max_length=10)
    image=models.ImageField()
    username=models.CharField(max_length=35)
    password= models.CharField(max_length=20)
        


class patientloginmodel(models.Model):
    username=models.CharField(max_length=35)
    password= models.CharField(max_length=20)


class patientappointmentmodel(models.Model):
    name=models.CharField(max_length=35)
    phone_no=models.CharField(max_length=12)
    hsptlname=models.CharField(max_length=35)
    date=models.DateField()
    timings=models.TimeField()

    