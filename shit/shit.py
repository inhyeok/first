#!/usr/bin/python
#-*- coding: utf-8 -*-
from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/shit')
def shit():
  m_list = [u'강원태', u'김영민', u'김준기', u'김준영', u'류경엽', u'박기완', u'박도현', u'박선주', u'박지원', u'유동영', u'윤여현', u'윤정현', u'이재호', u'전윤성', u'정민혁', u'정인혁', u'정효찬', u'최예닮', u'최준혁', u'홍정현']
  r_list = []
  for x in xrange(0,len(m_list)):
    ran = random.randint(0,len(m_list)-1)
    r_list.append(m_list[ran])
    m_list.pop(ran)
  return render_template('shit.html', m_list=r_list)

if __name__ == "__main__":
  app.run(debug=True, port=1212)