from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']


    description = forms.CharField(label = 'Description' ,widget=forms.Textarea())
    quantity = forms.IntegerField(label = 'Quantity' , widget=forms.NumberInput())
