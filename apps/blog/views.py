# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
def index(request):
	#response = "Hello, I am your first request!"
	return render(request, "blog/index.html")

def new(request):
	return render(request, "blog/new.html")

def create(request):
	return redirect("/")

def show(request, number):
	response = "show" + str(number)
	return HttpResponse(response)

def edit(request, number):
	response = "edit" + str(number)
	return HttpResponse(response)

def destroy(request, number):
	response = "destroy" + str(number)
	return redirect("/")
#def
# Create your views here.
