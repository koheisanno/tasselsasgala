# Generated by Django 2.2.6 on 2019-10-28 14:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('userid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('first_Name', models.CharField(default=' ', max_length=50)),
                ('last_Name', models.CharField(default=' ', max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('number_of_Guests', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
