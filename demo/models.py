from django.db import models

class Employee(models.Model):

	name = models.CharField(max_length=50)
	email = models.EmailField()
	mobile = models.BigIntegerField()
	salary = models.IntegerField()
	Address = models.TextField()
	class Meta:
		db_table = 'employee'


