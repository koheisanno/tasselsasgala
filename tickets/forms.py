from django import forms
from event import models

class Purchase(forms.ModelForm):
    class Meta:
        model=models.Person
        fields=['first_Name', 'last_Name', 'email', 'number_of_Guests']