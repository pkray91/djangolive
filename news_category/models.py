from django.db import models

# Create your models here.


class NewsCategory(models.Model):

	categoty = models.CharField(max_length=50)

	class Meta:
		db_table='newscategory'