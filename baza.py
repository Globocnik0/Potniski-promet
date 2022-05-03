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

#USTVARJANJE TABEL -----------------------

komanda = zbrisiTabelo("progekraji")
pozeni(komanda)
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
komanda = ustvariTabeloProgeKraji()
#pozeni(komanda)


#----POLNJENJE TABEL----------------

komanda = izbrisiCeloTabelo("voznired")
#pozeni(komanda)

komanda = napolniTabeloModel()
#pozeni(komanda)
print("tabela Model napolnjena")

komanda = napolniTabeloVlak(conn, cur, 30)
#pozeni(komanda)
print("tabela Vlak napolnjena")

komanda = napolniTabeloPostaja()
#pozeni(komanda)
print("tabela Postaja napolnjena")

komanda = napolniTabeloZaposleni(20)
#pozeni(komanda)
print("tabela Zaposleni napolnjena")

komanda = napolniTabeloPregled(cur, 40)
#pozeni(komanda)
print("tabela Pregled napolnjena")

komanda = napolniTabeloVozovnica()
#pozeni(komanda)
print("tabela Vozovnica napolnjena")

komanda = napolniTabeloPotnik(cur, 20)
#pozeni(komanda)
print("tabela Potnik napolnjena")

komanda = napolniTabeloProga(cur)
#pozeni(komanda)
print("tabela Proga napolnjena")

komanda = napolniTabeloProgeKraji(cur)
#pozeni(komanda)
print("tabela ProgeKraji napolnjena")

komanda = napolniTabeloVozniRed(cur)
#pozeni(komanda)
print("tabela VozniRed napolnjena")



