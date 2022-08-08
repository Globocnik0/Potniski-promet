# import sys
# sys.path.append("../../osnove_podatkovnih_baz")
# from osnove_podatkovnih_baz.iskanjeVoznegaReda import *
from iskanjeVoznegaReda import *
from prijavaNakup import *
import re

import bottle
import os
import shutil

app = bottle.default_app()
bottle.BaseTemplate.defaults['get_url'] = app.get_url


@bottle.route('/webpage/database/<filename:path>', name='database')
def serve_static_icon(filename):
    return bottle.static_file(
        filename, root=os.path.join(os.getcwd(), "database"))



@bottle.get('/')
def redirect():
    bottle.redirect('/search/')

@bottle.get('/search/')
def search_get():
    return bottle.template('search_engine.tpl')

@bottle.post('/search/')
def search():
    station_1 = bottle.request.forms['station_1']
    station_2 = bottle.request.forms['station_2']
    print(poisciVozniRed22(station_1, station_2))
    return bottle.template('display_traffic.tpl', traffic_data = poisciVozniRed22(station_1, station_2))


@bottle.get('/login/')
def login():
    return bottle.template('login.tpl', alert='')

@bottle.post('/login/')
def login_post():
    emso = bottle.request.forms['emso']
    username = bottle.request.forms['ime']
    rojstvo = bottle.request.forms['rojstvo']
    naslov = bottle.request.forms['naslov']
    email = bottle.request.forms['email']
    password = bottle.request.forms['password']
    first_time_user = bottle.request.forms.first_login
    if first_time_user == 'on':
        if re.search("^[A-Za-z0-9]*$", username) and re.search("^[A-Za-z0-9]*$",password):
            if registracijaUporabnika([emso, username, rojstvo, naslov, email, password]): #there is an error in this line
                bottle.redirect('/')
            else:
                return bottle.template('login.tpl', alert='Your EMŠO or email are already registred')
        else:
            return bottle.template(
                'login.tpl',
                alert='Only permitted characters are A-Z, a-z, 0-9.')
    else:
        if prijava(username, password):
            bottle.response.set_cookie('Logged', username)
            bottle.redirect('/')
        else:
            return bottle.template('login.tpl', alert = prijava(username, password))
    return bottle.template('login.tpl', alert='')



bottle.run(debug=True, reloader=True, host = "localhost", port = 8081)
