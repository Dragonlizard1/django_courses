# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
def create(request):
	response = "placeholder for users to create a new user record"
	return render(response)

def login(request):
	response = "placeholder for users to login"
	return render(response)

def new(request):
	response = "placeholder to add user or register"
	return render(response)

def display(request):
	response = "placeholder to later display all the list of users"
	return render(response)

#def
# Create your views here.
