from django import forms
from .models import Worker

class AddWorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ("name", "position", "branch")
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'position':forms.TextInput(attrs={'class':'form-control'}),
            'branch':forms.TextInput(attrs={'class':'form-control'}),
        }