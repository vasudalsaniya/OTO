from django import forms
from .models import Repairtable
from vehicle.models import Vehicle

class RepairForm(forms.ModelForm):
    class Meta:
        model=Repairtable
        fields=('__all__')
    