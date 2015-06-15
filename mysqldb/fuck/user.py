#-*- encoding:utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
import MySQLdb
import hashlib

app = Flask(__name__)

db_sv = 'localhost'
db_user = 'root'
db_pw = 'partcarry'
db_name = 'test'

conn = MySQLdb.connect(db_sv, db_user, db_pw, db_name)
cursor = conn.cursor()

def alertme(string):
  return "<script>alert('"+ string +"');</script>", redirect(url_for('main'))

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/main')
def main():
  return render_template('main.html')

@app.route('/signinw')
def signinw():
  return render_template('signin.html')
@app.route('/signin', methods=['POST'])
def signin():
  try:
    u_id = request.form['u_id']
    u_pw = request.form['u_pw']
    hs_pw = hashlib.sha1(u_pw).hexdigest()
    cursor.execute("INSERT INTO users(u_id, u_pw) VALUES ('%s','%s');" % (u_id, hs_pw))
    conn.commit()
    return alertme('Success signin!!')
  except:
    return alertme('Error!!!!')

@app.route('/loginw')
def loginw():
  return render_template('login.html')
@app.route('/login', methods=['POST'])
def login():
  u_id = request.form['u_id']
  u_pw = request.form['u_pw']
  hs_pw = hashlib.sha1(u_pw).hexdigest()
  try:
    cursor.execute("SELECT * FROM users;")
    row = cursor.fetchall()
    for i in row:
      if u_id == i[0]:
        for j in row:
          if hs_pw == j[1]:
            return alertme('Success login!!!')
          else:
            return alertme('Wrong pw...')
    return alertme('miss or wrong id...')
  except:
    return alertme('Error!!!!')

if __name__ == "__main__":
  app.run(debug=True, port=2345)