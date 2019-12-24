from django.db import models

class BodyInfo(models.Model):
	name = models.CharField(max_length=10)
	h = models.IntegerField(default=150)
	w = models.IntegerField(default=50)

	def __str__(self):
		return self.name
