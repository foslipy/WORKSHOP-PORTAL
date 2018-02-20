from flask import Flask
from flask import render_template, request, flash, redirect, session, abort
import MySQLdb
import os

db = MySQLdb.connect("localhost","root","shrey1234","shrey")


app = Flask(__name__)

@app.route("/")
def index():
	return render_template("home.html")

'''@app.route('/signupform')
def about():
    return render_template("signupform.html")

@app.route('/loginform')
def loginform():
    return render_template("loginform.html")
'''

@app.route('/adminview',methods = ['POST', 'GET'])
def adminview():
	'''if request.method == 'POST':
		result = request.form
		return render_template("adminview.html",result = result)'''
	if request.form['psw'] == 'admin2018' and request.form['email'] == 'admin@2018.com':
		session['logged_in'] = True
		result = request.form
		return render_template("adminview.html",result = result)
	else:
        	flash('wrong password!')
	return render_template("home.html")


@app.route('/freeform')
def freeform():
	return render_template("freeform.html")

		


@app.route('/result', methods = ['POST', 'GET'])
def result():

	if request.method=='POST':
		College_Name = request.form['Colname']
		Location = request.form['loc']
		HOD_Name = request.form['hod']
		Contact_Details = request.form['con']
		Seminar_Date = request.form['date']
		Topic = request.form['top']
		Expectation = request.form['expect']
	
		cursor = db.cursor()
		cursor.execute("""
	INSERT INTO Free_Workshop(College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Expectation) 
	VALUES (%s,%s,%s,%s,%s,%s,%s) """, (College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Expectation))
		db.commit()
		#msg = "Record successfully added"
		#return render_template("freeworkshoptable.html",msg = msg)

	cursor = db.cursor()
	cursor.execute("select * from Free_Workshop")
	data=cursor.fetchall()
    	return render_template("freeworkshoptable.html",data = data)
	
	db.close()
 
@app.route('/edit')
def edit():
	return render_template("freeform2.html")


@app.route('/editedresult', methods = ['POST', 'GET'])
def editedresult():

	if request.method=='POST':
		College_Name = request.form['Colname']
		Location = request.form['loc']
		HOD_Name = request.form['hod']
		Contact_Details = request.form['con']
		Seminar_Date = request.form['date']
		Topic = request.form['top']
		Expectation = request.form['expect']
	
		cursor = db.cursor()
		cursor.execute("""
	UPDATE Free_Workshop set College_Name='College_Name',Location='Location',HOD_Name='HOD_Name',Contact_Details='Contact_Details',Seminar_Date='Seminar_Date',Topic='Topic',Expectation='Expectation' 
	where College_Name='College_Name',Location='Location',HOD_Name='HOD_Name',Contact_Details='Contact_Details',Seminar_Date='Seminar_Date',Topic='Topic',Expectation='Expectation'""")
		db.commit()
		msg = "Record successfully updated"
		return render_template("return.html",msg = msg)

	'''cursor = db.cursor()
	cursor.execute("select * from Free_Workshop")
	db.commit()
	data=cursor.fetchall()
    	return render_template("freeworkshoptable.html",data = data)
	
	db.close()'''
	
'''   
@app.route('/freeworkshoptable')
def freeworkshoptable():
	cursor = db.cursor()
	cursor.execute("select * from Free_Workshop")
	data=cursor.fetchall()
    	return render_template("freeworkshoptable.html",row=row)
	db.close()'''
    




if (__name__ == "__main__"):
	app.secret_key = os.urandom(12)
	app.run(debug=True)
