# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class users(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class books(models.Model):
	name = models.CharField(max_length = 255)
	desc = models.CharField(max_length = 255)
	liked_user = models.ManyToManyField(users, related_name="liked_book")
	uploaded_by = models.ForeignKey(users, related_name="uploaded_books")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	

