from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import time 

app = Flask(__name__)
mysql = MySQLConnector(app,'users')

@app.route('/')
def index():
	return redirect ("/users")

@app.route('/users')
def mainindex():
	query = "SELECT * FROM users"    # define your query
	users = mysql.query_db(query) # run query with query_db()
	
	return render_template('index.html', users = users)

@app.route('/users/<user_id>')
def show(user_id):

	query = "SELECT * FROM users WHERE idusers = :id"    # define your query

	data = {
		'id': int(user_id)	
	}
	users = mysql.query_db(query, data) # run query with query_db()
	
	return render_template('show.html', users = users)

@app.route('/users/new')
def create():

	toggle = "new"
	return render_template('add_delete.html', toggle = toggle)

@app.route('/users/create', methods=['POST'])
def process_new():
	query = "INSERT INTO users (f_name, l_name, email, created_at) VALUES (:f_name, :l_name, :email, NOW())"
	
	data = {
	
		'f_name': request.form['f_name'],
		'l_name': request.form['l_name'],	
		'email': request.form['email']
		
	}
	
	mysql.query_db(query, data)
	
	return redirect('/users')

@app.route('/users/<user_id>/edit')
def update(user_id):

	query = "SELECT * FROM users WHERE idusers = :id"    # define your query
	data = {
		'id': int(user_id)	
	}
	users = mysql.query_db(query, data) # run query with query_db()
	

	toggle = "edit"
	return render_template('add_delete.html', users= users, toggle = toggle)


@app.route('/update/<user_id>', methods=['POST'])
def update2(user_id):
	query = "UPDATE users SET f_name = :first_name, l_name = :last_name, email = :email WHERE idusers = :id"
	data = {
		'first_name': request.form['f_name'],
		'last_name':  request.form['l_name'],
		'email': request.form['email'],
		'id': int(user_id)
	}
	mysql.query_db(query, data)
	return redirect('/')

@app.route('/users/<user_id>/destroy')
def delete(user_id):
	query = "SELECT * FROM users WHERE idusers = :id"    # define your query
	data = {'id': int(user_id)}
	users = mysql.query_db(query, data) # run query with query_db()
	
	toggle = "delete"
	return render_template('add_delete.html', users = users, toggle = toggle)


@app.route('/destroy/<user_id>', methods=['POST'])
def delete2(user_id):
	query = "DELETE FROM users WHERE idusers = :id"
	data = {'id': int(user_id)}
	mysql.query_db(query, data)

	return redirect('/')





app.run(debug=True)

