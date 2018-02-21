# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from time import gmtime, strftime
from django.utils.crypto import get_random_string 
import random
import time

def index(request):
	if "mygold" not in request.session:
		 request.session["mygold"] = 0
		 request.session["activity1"] = []

	return render(request, "NinjaGold/index.html")

def processmoney(request):
	
	if request.POST["building"] == "farm":
		value1 = random.randint(10, 21)
		request.session["mygold"] += value1 
		
		htmlString = "Earned "+ str(value1) + " golds from the farm! " + time.strftime('(%Y/%m/%d) %I:%M %p')
		request.session["activity1"].append([htmlString, "pos"] )

	elif request.POST["building"] == "cave":
		value1 = random.randint(5, 10)
		request.session["mygold"] += value1
		
		htmlString = "Earned "+ str(value1) + " golds from the cave! " + time.strftime('(%Y/%m/%d) %I:%M %p')
		request.session["activity1"].append([htmlString, "pos"])

	elif request.POST["building"] == "house":
		value1 = random.randint(2, 5)
		request.session["mygold"] += value1
		request.session["winloss"] = "pos"
		htmlString = "Earned "+ str(value1) + " golds from the house! " + time.strftime('(%Y/%m/%d) %I:%M %p')
		request.session["activity1"].append([htmlString, "pos"])

	elif request.POST["building"] == "casino":
		value1 = random.choice([-(random.randint(0, 50)), random.randint(0,50)] )
		if value1 < 0:
			winloss = "neg"
		else:
			winloss = "pos"

		if (request.session["mygold"] + value1) < 0:
			request.session["mygold"] = 0			
		else:
			request.session["mygold"] += value1
		
		htmlString = "Earned "+ str(value1) + " golds from the casino! " + time.strftime('(%Y/%m/%d) %I:%M %p')
		request.session["activity1"].append([htmlString, winloss])
	
	request.session["activity1"] = request.session["activity1"]
	print request.session["activity1"]
	return redirect("/")

#reset function to clear data session manually or with button


def reset(request):
	if "mygold" in request.session:	
		request.session.pop("mygold")
	if "activity1" in request.session:	
		request.session.pop("activity1")
	return redirect("/")







