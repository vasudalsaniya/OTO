from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields = ('cost_per_km','price','registration_plate','no_of_km_travelled','mileage','image','my_location')