from django.db import models



class SliderModel(models.Model):

	name = models.CharField(max_length=50)
	image = models.FileField()

	class Meta:
		db_table = 'slider'

	def __str__(self):

		return self.name
