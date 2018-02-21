# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from time import gmtime, strftime


def index(request):

  context = {
  "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
  }
  return render(request,'time_display/index.html', context)

'''
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
'''