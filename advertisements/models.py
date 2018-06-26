from django.db import models
from django import forms


from core.models import TimestampedModel

# Create your models here.



class Advertisement(TimestampedModel):
	
	type = forms.ModelChoiceField(widget=forms.RadioSelect, queryset=PaymentMethods.objects.all(), label='')




class AdvertisementType(models.Model):

	name = CharField(max_lenght=255)

	def __str__(self):
		return self.name



class PaymentMethods(models.Model):

	name = CharField(max_lenght=255)

	def __str__(self):
		return self.name