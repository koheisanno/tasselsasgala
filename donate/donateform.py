from django import forms
from donate.models import Donation, DonationCount

class Donate(forms.ModelForm):
    class Meta:
        model=Donation
        fields=['donation_type','number_of_items','your_donation','first_Name','last_Name','email','cover_the_transaction_fee']
        #fields=['number_of_item_1','number_of_item_2','number_of_item_3','number_of_item_4','your_donation','first_Name','last_Name','email']
        labels = {'donation_type':'I want to support: ',
        'cover_the_transaction_fee': "Make my donation go further. Raise my donation by 2.4% to cover the transaction fee."
        }
        