from django import forms
from .models import hospitalregistermodel

class hospitalregisterform(forms.ModelForm):
    class Meta:
        model = hospitalregistermodel
        fields = "__all__"
    def save(self):
        s=super().save(commit=False)
        s.password=make_password(self.cleaned_data['password'])
        s.save()
        return s


