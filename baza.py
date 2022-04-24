import auth
from baze import *
from simulacijaPodatkov import *
import psycopg2, psycopg2.extensions, psycopg2.extras

psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)

import csv



conn = psycopg2.connect(dbname = auth.db, host = auth.host, user = auth.user, password = auth.password)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
tabele = []

def pozeni(komanda):
    cur.execute(komanda)
    conn.commit()

#ustvarjanje baze -----------------------

#komanda = zbrisiTabelo("vlak")

komanda = ustvariTabeloModel()
#pozeni(komanda)
komanda = ustvariTabeloVlak()
#pozeni(komanda)
komanda = ustvariTabeloZaposlen()
#pozeni(komanda)
komanda = ustvariTabeloPregled()
#pozeni(komanda)
komanda = ustvariTabeloVozovnica()
#pozeni(komanda)
komanda = ustvariTabeloPotnik()
#pozeni(komanda)
komanda = ustvariTabeloPostaja()
#pozeni(komanda)
komanda = ustvariTabeloVoznja()
#pozeni(komanda)
komanda = ustvariTabeloProga()
#pozeni(komanda)
komanda = ustvariTabeloVozniRed()
#pozeni(komanda)

#----POLNJENJE TABEL----------------
komanda = izbrisiCeloTabelo("model")
pozeni(komanda)
komanda = napolniTabeloModel(vnosModel)
pozeni(komanda)
komanda = napolniTabeloVlak(conn, cur, 30)
pozeni(komanda)