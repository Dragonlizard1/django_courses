# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]$')
NAME_REGEX = re.compile(r'^[a-zA-Z]$')
PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9]$')

# Create your models here.
class checkManager(models.Manager):
	def reg_validator(self, postData):
		errors = {}
		for element, data in postData.iteritems():
			print data
		if len(postData['f_name']) <= 2:
			errors["first_name"] = "First Name should be more than 2 characters"

		if NAME_REGEX.match(postData['f_name']):
			errors["first_name"] = "First Name should be characters only"

		if len(postData['l_name']) <= 2:
			errors["last_name"] = "Last Name should be more than 2 characters"

		if NAME_REGEX.match(postData['l_name']):
		
			errors["last_name"] = "Last Name should be characters only"

		if EMAIL_REGEX.match(postData['email']):
			errors["email"] = "Email should be format correctly"

		if PASSWORD_REGEX.match(postData['password']):
			errors["password"] = "Password should be characters and numbers only"

		if len(postData['password']) <= 8:
			errors["password"] = "Password should be more than 8 characters"
		
		return errors

	def login_validator(self, postData):
		errors = {}
		if EMAIL_REGEX.match(postData['email']):
			errors["email"] = "Email should be format correctly"
		if PASSWORD_REGEX.match(postData['password']):
			errors["password"] = "Password should be characters and numbers only"
		if len(postData['password']) <= 8:
			errors["password"] = "Password should be more than 8 characters"
		
		if len(errors):
			return errors

		
		data1 = users.objects.get(email_address = postData["email"]).email_address
	
		if postData["email"] != data1:
			errors["email"] = "Email is incorrect"
		else:
			userpass = users.objects.get(email_address = postData["email"]).password
			if bcrypt.checkpw(postData["password"].encode(), userpass.encode()):
				return errors
			else:
				errors["password"] = "password is incorrect"

		return errors

		

	def data_create(self, postData):
		hash1 = bcrypt.hashpw(postData["password"].encode(), bcrypt.gensalt())
		users.objects.create(first_name = postData["f_name"],
			last_name = postData["l_name"],
			email_address = postData["email"],
			password = hash1,
			)
		return



class users(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email_address = models.CharField(max_length = 255)
	password = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at =  models.DateTimeField(auto_now = True)

	objects = checkManager()