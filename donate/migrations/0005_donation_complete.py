# Generated by Django 2.2.6 on 2019-11-02 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0004_donation_cover_the_transaction_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
