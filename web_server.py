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

@bottle.get('/')#tole prej ni blo tko
def redirect():
    bottle.redirect('/search/')

@bottle.get('/search/')
def search_get():
    emso = bottle.request.get_cookie('Logged')
    return bottle.template('search_engine.tpl', user = emso)

@bottle.post('/search/')
def search():
    station_1 = bottle.request.forms['station_1']
    station_2 = bottle.request.forms['station_2']
    return bottle.template('display_traffic.tpl', traffic_data = poisciVozniRed22(station_1, station_2))


@bottle.get('/register/')
def register():
    return bottle.template('register.tpl', alert='')

@bottle.post('/register/')
def register_post():
    emso = bottle.request.forms['emso']
    username = bottle.request.forms['ime']
    rojstvo = bottle.request.forms['rojstvo']
    naslov = bottle.request.forms['naslov']
    email = bottle.request.forms['email']
    password = bottle.request.forms['password']
    #first_time_user = bottle.request.forms.first_login
    if re.search("^[A-Za-z0-9]*$", username) and re.search("^[A-Za-z0-9]*$",password):
        if registracijaUporabnika([emso, username, rojstvo, naslov, email, password]): #dodal sm naslov
            bottle.template('login.tpl', alert='Now you can also log in')
        else:
            return bottle.template('register.tpl', alert='Your EMŠO or email are already registred')
    else:
        return bottle.template('register.tpl', alert='Only permitted characters are A-Z, a-z, 0-9.')


@bottle.get('/login/')
def login():
    return bottle.template('login.tpl', alert='')

@bottle.post('/login/')
def login_post():
    email = bottle.request.forms['email']
    password = bottle.request.forms['password']
    if prijava(email, password): #dodal sm naslov
        emso = dobiEmso(email)
        bottle.response.set_cookie('Logged', emso)
        bottle.redirect('/')
    else:
        return bottle.template('login.tpl', alert='Napačen email ali geslo')


@bottle.get('/uporabnik/<emso>/')
def uporabnik(emso):
    return "Čestitam za prijavo {0}".format(emso)

bottle.run(debug=True, reloader=True, host = "localhost", port = 8081) #dodal port pa localhost ker nevem koko točn to dela
