# Generated by Django 2.2.6 on 2019-11-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0002_auto_20191031_0516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='number_of_item_1',
            new_name='number_of_items',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='item_1',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='item_2',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='item_3',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='item_4',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='number_of_item_2',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='number_of_item_3',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='number_of_item_4',
        ),
        migrations.AddField(
            model_name='donation',
            name='donation_type',
            field=models.CharField(choices=[('general', 'general'), ('item1', 'item1 - $75 per ?'), ('item2', 'item 2 - $100 per ?'), ('item3', 'item 3 - $125 per ?'), ('item4', 'item 4 - $150 per ?')], default='general', max_length=50),
        ),
    ]
