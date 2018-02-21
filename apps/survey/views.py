# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
def create(request):
	response = "placeholder to display all the surveys created"
	return HttpResponse(response)

def new(request):
	response = "placeholder for users to add a new survey"
	return HttpResponse(response)


#def
# Create your views here.
