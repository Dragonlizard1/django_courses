# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from time import gmtime, strftime
from django.utils.crypto import get_random_string 

def start(request):
	return redirect("amadon/")

def index(request):

	if "quantity" not in request.session:
		request.session["quantity"] = 0 
		request.session["totalspent"] = 0.00

	pricing1 = 19.99
	pricing2 = 29.99
	pricing3 = 4.99
	product1 = {
		"id1" : "1",
		"item" : "Dojo Tshirt",
		"price" : pricing1}
	product2 = {
		"id1" : "2",
		"item" : "Dojo Sweater",
		"price" : pricing2,
	}
	product3 = {
		"id1" : "3",
		"item" : "Dojo Cup",
		"price" : pricing3,
	}
	request.session["products"] = []
	request.session["products"].append(product1)
	request.session["products"].append(product2)
	request.session["products"].append(product3)
	request.session["products"] = request.session["products"]

	return render(request,'Amadon/form.html')


def process(request):
	amount = request.POST["amount"]
	id_item = request.POST["product_id"]
	total =  float(request.POST["amount"]) * request.session["products"][int(id_item) - 1]["price"]
	request.session["total"] = total
	request.session["quantity"] += int(amount)
	request.session["totalspent"] += total

	return redirect("amadon/checkout/")

def result(request):

	return render(request,'amadon/result.html')
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