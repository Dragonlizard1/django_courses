# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from time import gmtime, strftime
from django.utils.crypto import get_random_string 


def index(request):

	return render(request,'SessionWord/form.html')

def process(request):


	
	if 'bigsize' in request.POST:
		bigsizeSet = "50px"
	else:
		bigsizeSet = "25px"

	content1 = {
	"word" : request.POST["word"],
	"color" : request.POST["color1"],
	"size" : bigsizeSet,	
	"time": "added on " + strftime("%H:%M %p, %m-%d-%Y", gmtime())
	}
	if "list" not in request.session:
		request.session["list"] = []

	request.session["list"].append(content1)
	request.session["list"] = request.session["list"]


	print request.session["list"]
	return redirect("/")

def cleaning(request):
	
	request.session.pop("list")

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