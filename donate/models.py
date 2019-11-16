from django.db import models
INT_CHOICES = [(x, x) for x in range(1, 60)]
DONATION_TYPE = (('general', 'general'), ('item1', 'Student Transportation'), ('item2', 'School Materials'), ('item3', 'School Building'), ('item4', 'Medicine'))

class Donation(models.Model):
    first_Name = models.CharField(default="first", max_length=50)
    last_Name = models.CharField(default="last", max_length=50)
    email = models.EmailField(default="email@gmail.com")
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
    
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        donationCount = DonationCount.objects.first()
        donationCount.general+=self.your_donation
        donationCount.save()


class DonationCount(models.Model):
    item1 = models.PositiveIntegerField(default=0)
    item2 = models.PositiveIntegerField(default=0)
    item3 = models.PositiveIntegerField(default=0)
    item4 = models.PositiveIntegerField(default=0)
    general = models.PositiveIntegerField(default=0)