from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.forms import ModelForm


class Apartment(models.Model):
    address_text = models.CharField(max_length=200)
    balcony_rating = models.IntegerField(default=None, blank=True, null=True)
    kitchen_rating = models.IntegerField(default=None, blank=True, null=True)
    two_bath_rating = models.BooleanField(default=False)
    bath_rating = models.IntegerField(default=None, blank=True, null=True)
    see_in_rating = models.IntegerField(default=None, blank=True, null=True)
    view_rating = models.IntegerField(default=None, blank=True, null=True)
    location_rating = models.IntegerField(default=None, blank=True, null=True)
    commute_rating = models.IntegerField(default=None, blank=True, null=True)
    storage_rating = models.IntegerField(default=None, blank=True, null=True)
    storehouse_available = models.BooleanField(default=False)
    renovation_need = models.BooleanField(default=False)
    cool_rating = models.IntegerField(default=None, blank=True, null=True)
    size_kvm = models.IntegerField(default=None, blank=True, null=True)
    room_amount = models.IntegerField(default=None, blank=True, null=True)
    floor_amount = models.IntegerField(default=None, blank=True, null=True)
    sun_rating = models.IntegerField(default=None, blank=True, null=True)
    feeling_emma = models.IntegerField(default=None, blank=True, null=True)
    feeling_daniel = models.IntegerField(default=None, blank=True, null=True)
    kvm_price_start = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_start = models.IntegerField(default=None, blank=True, null=True)
    kvm_price_end = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_end = models.IntegerField(default=None, blank=True, null=True)
    parking_rating = models.IntegerField(default=None, blank=True, null=True)
    parking_cost_elec = models.IntegerField(default=None, blank=True, null=True)
    parking_cost = models.IntegerField(default=None, blank=True, null=True)
    association_rating = models.IntegerField(default=None, blank=True, null=True)
    owns_land = models.BooleanField(default=False)
    build_year = models.DateField(datetime.datetime(1900, 1, 1), blank=True, null=True)
    association_kvm_loan = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    association_loan = models.BigIntegerField(default=False, blank=True, null=True)
    association_total_kvm = models.IntegerField(default=False, blank=True, null=True)
    tv_rating = models.IntegerField(default=False, blank=True, null=True)
    rent_cost = models.IntegerField(default=False, blank=True, null=True)
    view_date = models.DateField('date published')
#Nya datafält: hemnet länk. Varit på visning? När är visningen? Länk till booli

class ApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'


class Upcoming_app(models.Model):
    address_text = models.CharField(max_length=200, db_column='Address')
    balcony_rating = models.IntegerField(default=None, blank=True, null=True, db_column='Rating of balcony')
    kitchen_rating = models.IntegerField(default=None, blank=True, null=True)
    two_bath_rating = models.BooleanField(default=False, db_column='Two bathrooms')
    bath_rating = models.IntegerField(default=None, blank=True, null=True)
    see_in_rating = models.IntegerField(default=None, blank=True, null=True, db_column='View insight rating')
    view_rating = models.IntegerField(default=None, blank=True, null=True, db_column='Rating of view')
    location_rating = models.IntegerField(default=None, blank=True, null=True)
    commute_rating = models.IntegerField(default=None, blank=True, null=True)
    storage_rating = models.IntegerField(default=None, blank=True, null=True)
    storehouse_available = models.BooleanField(default=False)
    renovation_need = models.BooleanField(default=False)
    cool_rating = models.IntegerField(default=None, blank=True, null=True)
    size_kvm = models.IntegerField(default=None, blank=True, null=True)
    room_amount = models.IntegerField(default=None, blank=True, null=True)
    floor_amount = models.IntegerField(default=None, blank=True, null=True)
    sun_rating = models.IntegerField(default=None, blank=True, null=True)
    feeling_emma = models.IntegerField(default=None, blank=True, null=True)
    feeling_daniel = models.IntegerField(default=None, blank=True, null=True)
    kvm_price_start = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_start = models.IntegerField(default=None, blank=True, null=True)
    kvm_price_end = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_end = models.IntegerField(default=None, blank=True, null=True)
    parking_rating = models.IntegerField(default=None, blank=True, null=True)
    parking_cost_elec = models.IntegerField(default=None, blank=True, null=True)
    parking_cost = models.IntegerField(default=None, blank=True, null=True)
    association_rating = models.IntegerField(default=None, blank=True, null=True)
    owns_land = models.BooleanField(default=False)
    build_year = models.DateField(datetime.datetime(1900, 1, 1), blank=True, null=True)
    association_kvm_loan = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    association_loan = models.BigIntegerField(default=False, blank=True, null=True)
    association_total_kvm = models.IntegerField(default=False, blank=True, null=True)
    tv_rating = models.IntegerField(default=False, blank=True, null=True)
    rent_cost = models.IntegerField(default=False, blank=True, null=True)
    view_date = models.DateField('date published')
#Nya datafält: hemnet länk. Varit på visning? När är visningen? Länk till booli