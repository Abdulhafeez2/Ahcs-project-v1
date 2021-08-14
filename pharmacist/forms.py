from django import forms
import django.forms.widgets


class Medication_Form(forms.Form):
    name=forms.CharField(required=True,max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    frequency=forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'class':'form-control'}))
    description=forms.CharField(required=True,widget=forms.Textarea(attrs={'class':'form-control','type':'date'}))
    start_date=forms.DateField(required=True,widget=django.forms.DateInput(attrs={'class':' form-control'}))
    end_date=forms.DateField(required=True,widget=forms.DateInput(attrs={'class':'form-control'}))


