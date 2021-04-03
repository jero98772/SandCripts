#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
fechas_flask - 2020 - por jero98772
fechas_flask - 2020 - by jero98772
intentar comparar el formato de salida de fecha  html concidiera con el de la libreria datetime de python  
"""
import datetime
from flask import Flask, render_template, request, flash, redirect ,session
app = Flask(__name__)
def tiemetest():
	if request.method == 'POST':
		cal = str(request.form["cal"])
		print("html day",cal,type(cal))
		hoy = datetime.datetime.today().strftime('%Y-%m-%d')
		print("datetime today",hoy,type(hoy))
		if hoy == cal:
			print("se puede operar")
	return render_template("testdate.html")
@app.route("/",methods=['GET','POST'])
def main():
	return  tiemetest()
if __name__=='__main__':
	app.run(debug=True,host="0.0.0.0")
