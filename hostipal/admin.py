from django.contrib import admin
from  .models import bloodbank,hospitalhomemodel
# Register your models here.

class bloodbankAdmin(admin.ModelAdmin):
    list_display=['name','phone_no','address','bloodavali']

class hospitalhomeAdmin(admin.ModelAdmin):
    list_display=['name','contact_no','specialy','address']

admin.site.register(bloodbank,bloodbankAdmin)
admin.site.register(hospitalhomemodel,hospitalhomeAdmin)