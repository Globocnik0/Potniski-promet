from functools import total_ordering
import sys
# sys.path.append("../../osnove_podatkovnih_baz")
# from osnove_podatkovnih_baz.iskanjeVoznegaReda import *
from iskanjeVoznegaReda import *

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
    print(poisciVozniRed2(station_1, station_2))
    return bottle.template('display_traffic.tpl', traffic_data = poisciVozniRed2(station_1, station_2))
    #bottle.redirect('/display_traffic/')


bottle.run(debug=True, reloader=True)
