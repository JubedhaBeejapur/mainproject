from django import forms
from .models import patientregistermodel,patientloginmodel,patientappointmentmodel
from django.contrib.auth.hashers import make_password

class patientregisterform(forms.ModelForm):
    class Meta:
        model = patientregistermodel
        fields = "__all__"
    def save(self):
        s=super().save(commit=False)
        s.password=make_password(self.cleaned_data['password'])
        s.save()
        return s

class patientloginform(forms.Form):
    username= forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)


class patientappointmentform(forms.ModelForm):
    class Meta:
        model = patientappointmentmodel
        fields = "__all__"