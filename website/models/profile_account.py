from django.contrib.auth.models import User
from django.db import models



class ProfileRegistration(models.Model):
	'''
	Author: Meghan Debity
	Purpose: Model for buying and selling user(s)
	'''
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	phone_number = models.IntegerField()
	payment_option = models.ForeignKey('Payment', on_delete=models.CASCADE)
	order_history = models.ForeignKey('Order', on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	class Meta:
		db_table = "user"
