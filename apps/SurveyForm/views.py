# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from time import gmtime, strftime
from django.utils.crypto import get_random_string 


def index(request):

	return render(request,'SurveyForm/form.html')

def process(request):
	request.session["name1"] = request.POST["name"]
	request.session["location1"] = request.POST["location"]
	request.session["language1"] = request.POST["language"]
	request.session["comment1"] = request.POST["comment"]

	return redirect("/result")

def result(request):

	return render(request, "SurveyForm/result.html")
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