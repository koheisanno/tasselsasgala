# Generated by Django 2.2.6 on 2019-10-27 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0018_auto_20191027_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donationcount',
            old_name='bicycle',
            new_name='item1',
        ),
        migrations.AlterField(
            model_name='donation',
            name='donation_type',
            field=models.CharField(choices=[('general', 'general'), ('item1', 'item1'), ('item2', 'item2'), ('item3', 'item3'), ('item4', 'item4')], default='general', max_length=50),
        ),
    ]
