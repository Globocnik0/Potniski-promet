import auth as auth
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


tabele = ["model", "vlak", "zaposlen", "pregled", "vozovnica", "potnik", "postaja", "voznja", "proga", "voznired", "progekraji"]

#izbrisiVse(cur, tabele)
#USTVARJANJE TABEL -----------------------

#dovoljenja()

# zbrisiTabelo(cur, "model")
# zbrisiTabelo(cur, "vlak")
# zbrisiTabelo(cur, "zaposlen")
# zbrisiTabelo(cur, "pregled")
# zbrisiTabelo(cur, "vozovnica")
# zbrisiTabelo(cur, "potnik")
# zbrisiTabelo(cur, "postaja")
# zbrisiTabelo(cur, "voznja")
# zbrisiTabelo(cur, "proga")
# zbrisiTabelo(cur, "progekraji")
# zbrisiTabelo(cur, "voznired")
# zbrisiTabelo(cur, "uporabnik")
# zbrisiTabelo(cur, "kupljeneKarte")

# conn.commit()

# ustvariTabeloModel()
# ustvariTabeloVlak()
# ustvariTabeloZaposlen()
# ustvariTabeloPregled()
# ustvariTabeloVozovnica()
# ustvariTabeloPotnik()
# ustvariTabeloPostaja()
# ustvariTabeloVoznja()
# ustvariTabeloProgeKraji()
# ustvariTabeloVozniRed()
# ustvariTabeloUporabnik()
# ustvariTabeloKupljeneKarte()
# conn.commit()

#----POLNJENJE TABEL----------------
# izbrisiCeloTabelo(cur, "uporabnik")

# napolniTabeloModel(cur)
# print("tabela Model napolnjena")

# napolniTabeloVlak(cur, 30)
# print("tabela Vlak napolnjena")

# napolniTabeloPostaja(cur)
# print("tabela Postaja napolnjena")

# napolniTabeloZaposleni(cur, 20)
# print("tabela Zaposleni napolnjena")

# napolniTabeloVozovnica(cur)
# print("tabela Vozovnica napolnjena")

# napolniTabeloProgeKraji(cur)
# print("tabela ProgeKraji napolnjena")

# napolniTabeloVozniRed(cur)
# print("tabela VozniRed napolnjena")



conn.commit()