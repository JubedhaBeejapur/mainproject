from django.contrib import admin
from .models import patientregistermodel,patientappointmentmodel


# Register your models here.

class patientregistermodelAdmin(admin.ModelAdmin):
    list_display=['name','age','phone_no','gender','blood_grp','height','weight','material_status','image','username','password']

class patientappointmentmodelAdmin(admin.ModelAdmin):
    list_display=['name','phone_no','hsptlname','date','timings']

admin.site.register(patientregistermodel,patientregistermodelAdmin)
admin.site.register(patientappointmentmodel,patientappointmentmodelAdmin)
