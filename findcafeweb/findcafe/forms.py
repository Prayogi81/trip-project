from django.forms import ModelForm, widgets
from findcafe.models import Cafe
from django import forms

class CafeForm(ModelForm):
    class Meta:
        model = Cafe
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput({'class' : 'form-control'}),
            'location' : forms.TextInput({'class' : 'form-control'}),
            'wifi' : forms.TextInput({'class' : 'form-control'}),
            'toilet' : forms.TextInput({'class' : 'form-control'}),
            'smokingarea' : forms.TextInput({'class' : 'form-control'}),
            'ac_room' : forms.TextInput({'class' : 'form-control'}),
            'avg_price' : forms.TextInput({'class' : 'form-control'}),

        }