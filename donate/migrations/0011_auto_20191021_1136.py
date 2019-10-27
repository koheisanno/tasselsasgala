# Generated by Django 2.2.6 on 2019-10-21 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0010_auto_20191020_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donationcount',
            old_name='chairs',
            new_name='item2',
        ),
        migrations.AddField(
            model_name='donationcount',
            name='general',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=15),
        ),
        migrations.AddField(
            model_name='donationcount',
            name='item3',
            field=models.PositiveIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='donationcount',
            name='item4',
            field=models.PositiveIntegerField(default='0'),
        ),
    ]
