# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from time import gmtime, strftime
from django.utils.crypto import get_random_string 


def index(request):

	if "attempt" not in request.session:
		request.session["attempt"] = 0
		request.session["unique"] = ""

	return render(request,'randomm_word/index.html')

def new(request):
	request.session["attempt"] += 1
	request.session["unique"] = get_random_string(length=14)

	return redirect("/")

def reset(request):
	request.session["attempt"] = 0
	request.session["unique"] = ""

	return redirect("/")
'''

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
'''