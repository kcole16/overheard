from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator

from core.models import Account

class Topic(models.Model):
	title=models.CharField(max_length=1000, unique=True)
	timestamp=models.DateTimeField(auto_now_add=True)

	@classmethod
	def create(cls, title):
		topic = cls(title=title)
		return topic


class Location(models.Model):
	name=models.CharField(max_length=100)
	woeid=models.IntegerField()


class HypeComment(models.Model):
	@classmethod
	def create(cls, user, topic, content):
		comment = cls(user=user, topic=topic, content=content)
		return comment

	user = models.ForeignKey(Account)
	topic = models.ForeignKey(Topic)
	content = models.CharField(max_length=100)
	date_posted = models.DateTimeField(auto_now_add=True)



# Create your models here.
