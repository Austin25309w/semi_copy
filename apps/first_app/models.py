from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.

class userManager(models.Manager):
	def basic_validator(self, postData):
		errors ={}
		if len(postData['first_name']) <2:
			errors['first_name'] = "First Name should be at least 2 characters"
		if len(postData['last_name']) < 2:
			errors['last_name'] = "Last Name should be at least 2 characters"
		if len(postData['email']) < 1:
			errors['email'] = "please include email"
		if not EMAIL_REGEX.match(postData['email']):
			errors['email'] = "Please enter a valid email"
		return errors

class User(models.Model):
	first_name =models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email =	models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)

	objects = userManager()