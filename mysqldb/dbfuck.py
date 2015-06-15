#!/usr/bin/python
#-*- coding: utf-8 -*-
from flask import Flask, render_template, request
import MySQLdb
import hashlib

app = Flask(__name__)

db_sv = 'localhost'
db_user = 'root'
db_pw = 'partcarry'
db_name = 'test'

conn = MySQLdb.connect(db_sv, db_user, db_pw, db_name)
cursor = conn.cursor()

ID = 0
PW = 1

def alertme(string):
		return "<script>alert('"+ string +"');</script>"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/joinpage')
def joinpage():
	return render_template('join.html')
@app.route('/join', methods=['GET', 'POST'])
def join():
	try:
		u_id = request.form['u_id']
		u_pw = request.form['u_pw']
		hash_pw = hashlib.sha1(u_pw).hexdigest() #입력받은 비밀번호를 hash sha1 으로 암호화  hexdigest()는 값을 띄우는것
		cursor.execute("INSERT INTO users (u_id, u_pw) VALUES ('%s', '%s');" % (u_id, hash_pw))
		conn.commit()
		return render_template('index.html')

	except:
		return alertme("Error!!")

@app.route('/loginpage')
def loginpage():
	return render_template('login.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
	try:
		u_id = request.form['u_id']
		u_pw = request.form['u_pw']
		hash_pw = hashlib.sha1(u_pw).hexdigest()
		cursor.execute("SELECT * FROM users;")
		row = cursor.fetchall() #cursor 객체의 fetchone() 메소드를 호출하면 한 행에 대한 데이터가 Tuple 형태로 리턴 fetchall()은 모든 데이터를 가져
		for i in row:
			if u_id == i[ID]:
				if hash_pw == i[PW]:
					return alertme("login ok")
				else:
					return alertme("pw no")

		return alertme("id is missing or wrong")

	except:
		return alertme("Error!!")

if __name__ == "__main__":
	app.run(debug=True, port=1234)