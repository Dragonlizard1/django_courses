from flask import Flask, render_template, session, request, redirect
import random, time
app = Flask(__name__)    
app.secret_key = 'ThisIsSecretNinjaGold'  



@app.route("/")  
def index():
	if "mygold" not in session:
		 session["mygold"] = 0
		 session["activity1"] = []

	return render_template("index.html")


@app.route("/process_money", methods = ["POST"])  
def processmoney():
	
	if request.form["building"] == "farm":
		value1 = random.randint(10, 21)
		session["mygold"] += value1 
		
		htmlString = "Earned "+ str(value1) + " golds from the farm! " + time.strftime('(%Y/%m/%d) %I:%M %p')
		session["activity1"].append([htmlString, "pos"] )

	elif request.form["building"] == "cave":
		value1 = random.randint(5, 10)
		session["mygold"] += value1
		
		htmlString = "Earned "+ str(value1) + " golds from the cave! " + time.strftime('(%Y/%m/%d) %I:%M %p')
		session["activity1"].append([htmlString, "pos"])

	elif request.form["building"] == "house":
		value1 = random.randint(2, 5)
		session["mygold"] += value1
		session["winloss"] = "pos"
		htmlString = "Earned "+ str(value1) + " golds from the house! " + time.strftime('(%Y/%m/%d) %I:%M %p')
		session["activity1"].append([htmlString, "pos"])

	elif request.form["building"] == "casino":
		value1 = random.choice([-(random.randint(0, 50)), random.randint(0,50)] )
		if value1 < 0:
				winloss = "neg"
			else:
				winloss = "pos"
			if (session["mygold"] + value1) < 0:
				session["mygold"] = 0
			
		else:
			session["mygold"] += value1
		
		htmlString = "Earned "+ str(value1) + " golds from the casino! " + time.strftime('(%Y/%m/%d) %I:%M %p')
		session["activity1"].append([htmlString, winloss])
	

	return redirect("/")

#reset function to clear data session manually or with button

@app.route("/reset", methods = ["POST"])
def reset():
	if "mygold" in session:	
		session.pop("mygold")
	if "activity1" in session:	
		session.pop("activity1")
	return redirect("/")

@app.route("/reset1")
def reset1():
	if "mygold" in session:	
		session.pop("mygold")
	if "activity1" in session:	
		session.pop("activity1")
	return redirect("/")



app.run(debug=True)  
   

