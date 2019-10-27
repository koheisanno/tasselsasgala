from django.contrib import admin
from .models import Donation, DonationCount

admin.site.register(Donation)
admin.site.register(DonationCount)