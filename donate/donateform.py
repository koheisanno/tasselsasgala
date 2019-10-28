from django import forms
from donate.models import Donation, DonationCount

class Donate(forms.ModelForm):
    class Meta:
        model=Donation
        fields=['donation_type','number','your_donation']