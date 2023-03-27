# Generated by Django 4.1.1 on 2022-10-20 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lghter', '0002_apartment_owns_land_apartment_renovation_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='association_loan',
            field=models.BigIntegerField(default=False),
        ),
        migrations.AddField(
            model_name='apartment',
            name='association_rating',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='association_total_kvm',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='apartment',
            name='balcony_rating',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='bath_rating',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='build_year',
            field=models.DateTimeField(default='1900-01-01'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='commute_rating',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='cool_rating',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='feeling_daniel',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='feeling_emma',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='floor_amount',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='kitchen_rating',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='location_rating',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='parking_cost',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='parking_cost_elec',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='parking_rating',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='price_end',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='price_start',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='rent_cost',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='apartment',
            name='room_amount',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='see_in_rating',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='size_rating',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='storage_rating',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='sun_rating',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='apartment',
            name='tv_rating',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='apartment',
            name='view_rating',
            field=models.IntegerField(default=None),
        ),
    ]
