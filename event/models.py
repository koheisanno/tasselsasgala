from django.db import models
import uuid
from django.urls import reverse
import qrcode
from PIL import Image
from io import BytesIO
from django.core.files import File


BOOL_CHOICES = ((True, 'Attended'), (False, 'Absent'))
#BOOL_CHOICES_PAYMENT = ((True, 'Complete'), (False, 'Incomplete'))


class Person(models.Model):
    userid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    first_Name = models.CharField(default=" ", max_length=50)
    last_Name = models.CharField(default=" ", max_length=50)
    email = models.EmailField()
    number_of_Guests = models.PositiveIntegerField(default=0)
    url_link = models.CharField(default=' ', max_length=200)
    qr_image = models.ImageField(upload_to='qrcodes', default='default.jpg', blank=True, null=True)
    attended = models.BooleanField(default = False, choices=BOOL_CHOICES)
    #payment_complete = models.BooleanField(default = False, choices=BOOL_CHOICES_PAYMENT)

    def __str__(self):
        return (self.first_Name + " " + self.last_Name + " " + str(self.userid))
    
    def save(self, *args, **kwargs):
        self.url_link = "tasselsasgala.com/" + str(self.userid)
        img = qrcode.make(self.url_link)
        canvas = Image.new('RGB', (400, 400), 'white')
        canvas.paste(img)
        canvas = canvas.resize((300,300), Image.ANTIALIAS)

        blob = BytesIO()
        canvas.save(blob, 'JPEG')
        self.qr_image.save('qr-' + str(self.userid) + '.jpg', File(blob), save=False)
        super().save(*args, **kwargs)