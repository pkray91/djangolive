from django.db import models

class NewsModel(models.Model):

	categoty = models.CharField(max_length=50)
	head_line = models.CharField(max_length=50)
	image = models.FileField()
	detail_news = models.TextField()

	class Meta:
		db_table = 'news' 


	def __str__(self):
		return self.head_line
