# Generated by Django 4.1.1 on 2022-10-20 14:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lghter', '0003_apartment_association_loan_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apartment',
            old_name='renovation_rating',
            new_name='renovation_need',
        ),
        migrations.RenameField(
            model_name='apartment',
            old_name='size_rating',
            new_name='size_kvm',
        ),
        migrations.RenameField(
            model_name='apartment',
            old_name='storehouse_rating',
            new_name='storehouse_available',
        ),
        migrations.AlterField(
            model_name='apartment',
            name='build_year',
            field=models.DateField(verbose_name=datetime.datetime(1900, 1, 1, 0, 0)),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='view_date',
            field=models.DateField(verbose_name='date published'),
        ),
    ]