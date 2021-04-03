#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
encriptar_de_a_usuario_flask - 2020 - por jero98772
encriptar_de_a_usuario_flask - 2020 - by jero98772
"""
from flask import Flask, render_template, request, flash, redirect ,session
from Crypto.Cipher import AES
from Crypto import Random
import sqlite3
import base64
from hashlib import sha256
import random as rnd
BLOCK_SIZE = 16
app = Flask(__name__)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
def enPassowrdHash(password):
	hashPassowrd = sha256(password.encode("utf-8")).digest()
	return hashPassowrd
def enPassowrdStr(password):
	hashPassowrd = str(sha256(password.encode('utf-8')).digest())
	return hashPassowrd
def generatePass():
	passowrdStr = ""
	for i in range(0,16):
		n = rnd.randint(0,9999)
		n = str(hex(n))
		if len(passowrdStr) >= 16 and len(passowrdStr)-len(n) <= 16:
			passowrdStr += n
			break
		return enPassowrdStr(passowrdStr)
# el desorden no es definitivo en hackido cambia gracias :-)
app.secret_key =  str(generatePass())
app.config['SECRET_KEY']
def encrypt(text, password):
    private_key = enPassowrdHash(password)
    text = pad(text)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(text))
def decrypt(text, password):
    private_key = enPassowrdHash(password)
    text = base64.b64decode(text)
    iv = text[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    mensaje =  unpad(cipher.decrypt(text[16:]))
    return mensaje.decode()
def busquedageneral(data):
	key = app.secret_key
	todosmsg = ""
	for i in data:
		print(i[0])
		msg = str(decrypt(i[0],key))
		todosmsg += msg 
		print(msg)
	return todosmsg
@app.route("/encriptar",methods=['GET','POST'])
def encriptarweb():
	connecting = sqlite3.connect("db_test")
	cursor = connecting.cursor()
	if request.method == 'POST':
		secreto = str(request.form["secreto"])
		key = app.secret_key#str(request.form["key"])
		#= enPassowrd(key)
		secreto = encrypt(secreto,key)
		cursor.execute("INSERT INTO test(data, pass) VALUES(?,?)",(secreto,key))#key es por ahora mientras se prueba
		cursor.connection.commit()
	return render_template("encriptar.html")
@app.route("/desencriptar",methods=['GET','POST'])
def desencriptarweb():
	connecting = sqlite3.connect("db_test")
	cursor = connecting.cursor()
	#if request.method == 'POST':
	cursor.execute("SELECT data FROM test")
	datos = cursor.fetchall()
	print(datos)
	mensajedec = busquedageneral(datos)
	return render_template("desencriptar.html",msgdec = mensajedec)
if __name__=='__main__':
	app.run(debug=True,host="0.0.0.0")
