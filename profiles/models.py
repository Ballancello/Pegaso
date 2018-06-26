from django.db import models

from core.models import TimestampedModel
from django.utils.translation import ugettext_lazy as _
from django.conf import settings 

class Profile(TimestampedModel):

	# There is an inherent relationship between the Profile and
	# User models. By creating a one-to-one relationship between the two, we
	# are formalizing this relationship. Every user will have one -- and only
	# one -- related Profile model.

	user = models.OneToOneField('authentication.User', on_delete=models.CASCADE)

	number_of_exchanges = models.PositiveIntegerField(default=0)
	commerce_volume = models.PositiveIntegerField(default=0)
	confirmations = models.PositiveIntegerField(default=0)
	punctuation = models.PositiveIntegerField(default=0)
	language = models.CharField(max_length=25,choices=settings.LANGUAGES,default='2')
	email_verification = models.DateTimeField(auto_now=True)
	phone_verification = models.DateTimeField(auto_now=True)
	trusted = models.ManyToManyField('self',related_name='trusted_by',symmetrical=False)
	blocked = models.ManyToManyField('self',related_name='blocked_by',symmetrical=False)



	def __str__(self):
		return self.user.username



