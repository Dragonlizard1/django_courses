# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime
from django.utils.crypto import get_random_string 
from .models import *
# Create your views here.
def index(request):
	
	return render(request, "Login_Reg/index.html" )

def register(request):
	errors = users.objects.reg_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect("/")
	else:
		users.objects.data_create(request.POST)

	name = request.POST["f_name"] + " " + request.POST["l_name"]
	return render(request, 'Login_Reg/success.html', {"name" : name})

def login(request):
	errors = users.objects.login_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect("/")
	else:

		print "inside"
	data = users.objects.get(email_address = request.POST['email'])
	name = data.first_name + " " + data.last_name
	return render(request, 'Login_Reg/success.html', {"name" : name})