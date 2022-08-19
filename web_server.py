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
    try:
        traffic_data = vozniredZRazdaljo(station_1, station_2)
    except:
        traffic_data = []
    return bottle.template('display_traffic.tpl', traffic_data = traffic_data, username = username)


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


@bottle.get('/ticket_preview/<station_1>/<station_2>/<type>/')
def preview_ticket(station_1, station_2, type):
    emso = bottle.request.get_cookie('Logged')
    if emso:
        username = informacijeUporabnika(emso)[0]
    else:
        bottle.redirect('/')
    if int(type) == 5:
        ticket_type = 'Daily ticket'
        faktor_cene = 1
    elif int(type) == 4:
        ticket_type = 'Student monthly ticket'
        faktor_cene = 20
    elif int(type) == 3:
        ticket_type = 'Monthly ticket'
        faktor_cene = 25
    elif int(type) == 2:
        ticket_type = 'Pensioner monthly ticket'
        faktor_cene = 0
    elif int(type) == 1:
        ticket_type = 'Yearly ticket'
        faktor_cene = 280

    price = vozniredZRazdaljo(station_1, station_2)[0][2] * 0.1 * faktor_cene # 5 centov na kilometer
    return bottle.template('ticket_preview.tpl', username = username, station_1 = station_1, station_2 = station_2, ticket_type = ticket_type, type = type, price = price)

@bottle.get('/buy_ticket/<station_1>/<station_2>/<type>/')
def uporabnik(station_1, station_2, type):
    emso = bottle.request.get_cookie('Logged')
    
    if int(type) == 5:
        ticket_type = 'Daily ticket'
        faktor_cene = 1
    elif int(type) == 4:
        ticket_type = 'Student monthly ticket'
        faktor_cene = 20
    elif int(type) == 3:
        ticket_type = 'Monthly ticket'
        faktor_cene = 25
    elif int(type) == 2:
        ticket_type = 'Pensioner monthly ticket'
        faktor_cene = 0
    elif int(type) == 1:
        ticket_type = 'Yearly ticket'
        faktor_cene = 280

    price = vozniredZRazdaljo(station_1, station_2)[0][2] * 0.1 * faktor_cene # 5 centov na kilometer
    nakupKarte([emso, station_1, station_2, type, price])
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
    


bottle.run(debug=True, reloader=True, host = "localhost", port = 8081) #dodal port pa localhost ker nevem koko točn to dela
