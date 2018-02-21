# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse

from time import gmtime, strftime
from django.utils.crypto import get_random_string 
from .models import *


#@app.route('/')
def index(request):
	return redirect ("/users")

#@app.route('/users')
def mainindex(request):


	return render(request, 'Semi_restful/index.html', {"users" : users.objects.all() })

#@app.route('/users/<user_id>')
def show(request, user_id):

	return render(request,'Semi_restful/show.html', {"users" : users.objects.get(id = int(user_id))})

#@app.route('/users/new')
def create(request):


	return render(request, 'Semi_restful/add_delete.html', {"toggle" : "new"})

#@app.route('/users/create', methods=['POST'])
def process_new(request):

	
	users.objects.create(first_name = request.POST['f_name'], last_name = request.POST['l_name'], email=  request.POST['email'])
	return redirect('/users')

#@app.route('/users/<user_id>/edit')
def update(request, user_id):
	content = {
	"toggle" : "edit",
	"users" : users.objects.get(id = int(user_id))
	}
	
	return render(request, 'Semi_restful/add_delete.html',content)


#@app.route('/update/<user_id>', methods=['POST'])
def update2(request, user_id):
	user1 = users.objects.get(id = int(user_id))

	user1.first_name = request.POST['f_name'],
	user1.last_name = request.POST['l_name'],
	user1.email =  request.POST['email'],
	user1.save()

	return redirect('/')

#@app.route('/users/<user_id>/destroy')
def delete(request, user_id):
	content = {
	"toggle" : "delete",
	"users" : users.objects.get(id = int(user_id))
	}
	return render(request, 'Semi_restful/add_delete.html', content)


#@app.route('/destroy/<user_id>', methods=['POST'])
def delete2(request, user_id):
	user1 = users.objects.get(id = int(user_id))
	user1.delete()

	return redirect('/')

def reset(request):
	del request.session["start"]
	return redirect("/")