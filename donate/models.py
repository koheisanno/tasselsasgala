from django.db import models
INT_CHOICES = [(x, x) for x in range(1, 60)]
DONATION_TYPE = (('general', 'general'), ('item1', 'item1'), ('item2', 'item2'), ('item3', 'item3'), ('item4', 'item4'))

class Donation(models.Model):
    first_Name = models.CharField(default=" ", max_length=50)
    last_Name = models.CharField(default=" ", max_length=50)
    email = models.EmailField()
    donation_type = models.CharField(default='general', max_length=50, choices=DONATION_TYPE)
    number = models.PositiveIntegerField(choices=INT_CHOICES, default='1')
    amount = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return (self.donation_type + self.first_Name + " " + self.last_Name)

class DonationCount(models.Model):
    item1 = models.PositiveIntegerField(default='0')
    item2 = models.PositiveIntegerField(default='0')
    item3 = models.PositiveIntegerField(default='0')
    item4 = models.PositiveIntegerField(default='0')
    general = models.DecimalField(max_digits=15, decimal_places=2, default='0')