# Generated by Django 2.2.6 on 2019-10-20 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0006_donation_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='amount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
