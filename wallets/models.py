from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.models import TimestampedModel
# from cryptographic_fields.fields import EncryptedCharField

# Create your models here.


class Wallet(TimestampedModel):

	profile = models.OneToOneField('profiles.Profile', on_delete=models.CASCADE)
	receiving_address = models.CharField(max_length=255)
	# transaction_number = models.IntegerField()
	private = models.CharField(max_length=255,default='')
	reg_private = models.CharField(max_length=255,default='')
	balance = models.DecimalField(max_digits=16,decimal_places=8,default=0)
	sent_transactions_30 = models.ForeignKey('wallets.SendBitcoins', on_delete=models.CASCADE, related_name = 'sent_transactions', null=True)
	received_transactions_30 = models.ForeignKey('wallets.ReceiveBitcoins',on_delete=models.CASCADE, related_name = 'receive_transactions', null=True)

	def __str__(self):

		return '{} - Wallet'.format(self.profile.user.email)

	def get_balance(self):

		return "BTC {}".format(self.balance)

	# def get_satoshis(self, btc):

	# 	btc = btc * (10**8)

	# 	return int(btc) 



class SendBitcoins(TimestampedModel):

	wallet = models.ForeignKey('wallets.Wallet',on_delete=models.CASCADE,related_name = 'send_wallet' )
	tx_ref = models.CharField(max_length=255,null=True, default='')
	to_ext_wallet = models.CharField(max_length=255,null=True, default='')
	amount = models.DecimalField(_('BTC'),max_digits=16,decimal_places=8, null=False)
	to_wallet = models.CharField(max_length=255,null=True, default='')
	description = models.TextField(_('Description'),null=True)

class ReceiveBitcoins(TimestampedModel):

	from_wallet = models.CharField(max_length=255)
	amount = models.DecimalField(max_digits=8,decimal_places=8)



# class Transactions(models.Model):

# 	sender = OneToOneField('wallets.SendBitcoins'. c)
# 	receiver = 


