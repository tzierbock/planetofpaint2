from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Canvas(models.Model):
	uuid = models.CharField(max_length=10, primary_key=True)
	title = models.CharField(max_length=50)

	players = models.ManyToManyField(User)

	def __unicode__(self):
		return self.title


class Point(models.Model):
	creation_time = models.DateTimeField()

	latitude = models.FloatField()
	longitude = models.FloatField()

	canvas = models.ForeignKey(Canvas, default=True)

	def __unicode__(self):
		return "Point"