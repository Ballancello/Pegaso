import requests

from django import forms 

from django.conf import settings

from django.contrib import messages
from django.utils.translation import ugettext_lazy as _ 

from .models import SendBitcoins




class SendBitcoinsCreateForm(forms.ModelForm):

	class Meta:

		model = SendBitcoins
		fields = [
			'amount',
			'to_wallet',
			'description'

		]

		widgets = {

			'amount' :forms.TextInput()
		}



