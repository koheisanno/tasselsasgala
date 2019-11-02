from django.db import models
INT_CHOICES = [(x, x) for x in range(1, 60)]
DONATION_TYPE = (('general', 'general'), ('item1', 'item1 - $75 per ?'), ('item2', 'item 2 - $100 per ?'), ('item3', 'item 3 - $125 per ?'), ('item4', 'item 4 - $150 per ?'))

class Donation(models.Model):
    first_Name = models.CharField(default=" ", max_length=50)
    last_Name = models.CharField(default=" ", max_length=50)
    email = models.EmailField()
    donation_type = models.CharField(default='general', max_length=50, choices=DONATION_TYPE)
    number_of_items = models.PositiveIntegerField(choices=INT_CHOICES, default=1)
    '''number_of_item_1 = models.PositiveIntegerField(choices=INT_CHOICES, default=1)
    number_of_item_2 = models.PositiveIntegerField(choices=INT_CHOICES, default=1)
    number_of_item_3 = models.PositiveIntegerField(choices=INT_CHOICES, default=1)
    number_of_item_4 = models.PositiveIntegerField(choices=INT_CHOICES, default=1)
    item_1 = models.PositiveIntegerField(default=0)
    item_2 = models.PositiveIntegerField(default=0)
    item_3 = models.PositiveIntegerField(default=0)
    item_4 = models.PositiveIntegerField(default=0)'''
    your_donation = models.PositiveIntegerField(null=True, blank=True, default=0)
    cover_the_transaction_fee=models.BooleanField(default=True)
    complete=models.BooleanField(default=False)


    def __str__(self):
        return (self.first_Name + " " + self.last_Name)

class DonationCount(models.Model):
    item1 = models.PositiveIntegerField(default=0)
    item2 = models.PositiveIntegerField(default=0)
    item3 = models.PositiveIntegerField(default=0)
    item4 = models.PositiveIntegerField(default=0)
    general = models.PositiveIntegerField(default=0)