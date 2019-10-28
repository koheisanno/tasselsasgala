# Generated by Django 2.2.6 on 2019-10-28 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(default=' ', max_length=50)),
                ('last_Name', models.CharField(default=' ', max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('donation_type', models.CharField(choices=[('general', 'general'), ('item1', 'item1 - $75 per ?'), ('item2', 'item 2 - $100 per ?'), ('item3', 'item 3 - $125 per ?'), ('item4', 'item 4 - $150 per ?')], default='general', max_length=50)),
                ('number_of_items', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59)], default=1)),
                ('your_donation', models.PositiveIntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DonationCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item1', models.PositiveIntegerField(default=0)),
                ('item2', models.PositiveIntegerField(default=0)),
                ('item3', models.PositiveIntegerField(default=0)),
                ('item4', models.PositiveIntegerField(default=0)),
                ('general', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
