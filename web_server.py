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


# @bottle.route('/webpage/database/<filename:path>', name='database')
# def serve_static_icon(filename):
#     return bottle.static_file(
#         filename, root=os.path.join(os.getcwd(), "database"))

@bottle.get('/')
def redirect():
    bottle.redirect('/search/')

@bottle.get('/search/')
def search_get():
    emso = bottle.request.get_cookie('Logged')
    if emso:
        username = informacijeUporabnika(emso)[0]
    else:
        username = False
    return bottle.template('search_engine.tpl', username = username)

@bottle.post('/search/')
def search():
    emso = bottle.request.get_cookie('Logged')
    if emso:
        username = informacijeUporabnika(emso)[0]
    else:
        username = False

    station_1 = bottle.request.forms['station_1']
    station_2 = bottle.request.forms['station_2']
    return bottle.template('display_traffic.tpl', traffic_data = vozniredZRazdaljo(station_1, station_2), username = username)


@bottle.get('/register/')
def register():
    if bottle.request.get_cookie('Logged'):
        bottle.redirect('/')
    return bottle.template('register.tpl', alert='', username = False)

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
            return bottle.template('login.tpl', alert='Now you can also log in', username = False) #a je čudno da na strani register dam template login?
        else:
            return bottle.template('register.tpl', alert='Your EMŠO or email are already registred', username = False)
    else:
        return bottle.template('register.tpl', alert='Only permitted characters are A-Z, a-z, 0-9.', username = False)


@bottle.get('/login/')
def login():
    if bottle.request.get_cookie('Logged'):
        bottle.redirect('/')
    return bottle.template('login.tpl', alert='', username = False)

@bottle.post('/login/')
def login_post():
    email = bottle.request.forms['email']
    password = bottle.request.forms['password']
    if prijava(email, password): #dodal sm naslov
        emso = dobiEmso(email)
        bottle.response.set_cookie('Logged', emso, path = '/')
        bottle.redirect('/')
    else:
        return bottle.template('login.tpl', alert='Napačen email ali geslo', username = False)

@bottle.get('/logout/')
def logout():
    bottle.response.set_cookie('Logged', '', path='/', expires=0)
    bottle.redirect('/')


@bottle.get('/buy_ticket/<station_1>/<station_2>/<type>/')
def uporabnik(station_1, station_2, type):
    emso = bottle.request.get_cookie('Logged')
    razdalja = vozniredZRazdaljo(station_1, station_2) #treba nekak izračunat ceno
    price = 2
    nakupKarte([emso, station_1, station_2, type, price])
    print('vstopnica nakupljena')
    bottle.redirect('/tickets/')


@bottle.get('/tickets/')
def display_tickets():
    emso = bottle.request.get_cookie('Logged')
    if emso:
        tickets = informacijeUporabnikaNakupi(emso)
        print(tickets)
        username = informacijeUporabnika(emso)[0]
        return bottle.template('display_tickets.tpl', username = username, tickets= tickets)
    else:
        bottle.redirect('/')
    

# @bottle.get('/uporabnik/<emso>/')
# def uporabnik(emso):
#     return "Čestitam za prijavo {0}".format(emso)

bottle.run(debug=True, reloader=True, host = "localhost", port = 8081) #dodal port pa localhost ker nevem koko točn to dela
