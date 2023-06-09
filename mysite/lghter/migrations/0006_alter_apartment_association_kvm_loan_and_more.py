# Generated by Django 4.1.1 on 2022-10-22 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lghter', '0005_alter_apartment_balcony_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='association_kvm_loan',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='association_loan',
            field=models.BigIntegerField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='association_rating',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='association_total_kvm',
            field=models.IntegerField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='bath_rating',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='build_year',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.datetime(1900, 1, 1, 0, 0)),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='commute_rating',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='cool_rating',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='feeling_daniel',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='feeling_emma',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='floor_amount',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='kitchen_rating',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='kvm_price_end',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='kvm_price_start',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='location_rating',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='parking_cost',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='parking_cost_elec',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='parking_rating',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='price_end',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='price_start',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='rent_cost',
            field=models.IntegerField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='room_amount',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='see_in_rating',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='size_kvm',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='storage_rating',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='sun_rating',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='tv_rating',
            field=models.IntegerField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='view_rating',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
