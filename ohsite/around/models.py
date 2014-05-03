from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator

from core.models import Account


class Post(models.Model):
	@classmethod
	def create(cls, user, content, date_posted):
		post = cls(user=user, content=content, date_posted=date_posted)
		return post

	user = models.ForeignKey(Account)
	content = models.CharField(max_length=500)
	date_posted = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
	@classmethod
	def create(cls, user, post, content, date_posted):
		comment = cls(user=user, post=post, content=content, date_posted=date_posted)
		return comment

	user = models.ForeignKey(Account)
	post = models.ForeignKey(Post)
	content = models.CharField(max_length=100)
	date_posted = models.DateTimeField(auto_now_add=True)



