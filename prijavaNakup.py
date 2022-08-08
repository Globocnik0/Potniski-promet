import auth
from baze import *
from simulacijaPodatkov import *
import psycopg2, psycopg2.extensions, psycopg2.extras
from tabulate import tabulate

psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)

import csv


conn = psycopg2.connect(dbname = auth.db, host = auth.host, user = auth.user, password = auth.password)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

def registracijaUporabnika(podatki): #podatki so [emso, ime, rojstvo, naslov, mail, geslo]
    cur.execute(""" SELECT mail from uporabnik where mail = %s """, [podatki[4]])
    mailObstaja = cur.fetchall()
    if mailObstaja:
        return False

    cur.execute(""" SELECT emso from uporabnik where emso = %s """,[podatki[0]])
    emsoObstaja = cur.fetchall()
    if emsoObstaja:
        return False

    print('registriran')
    cur.execute("""INSERT INTO uporabnik(emso, ime, rojstvo, naslov, mail, geslo) values (%s, %s, %s, %s, %s, %s)""", podatki)
    conn.commit()
    return True
        

def nakupKarte(podatki): #[emso, vrsta Karte], mejbi ne dela, mejbi pa dela
    
    emso = podatki[0]
    vrsta = podatki[1]
    cur.execute("""SELECT velja FROM vozovnica WHERE id = {} """.format(vrsta))
    velja = cur.fetchall()[0][0]
    cur.execute(""" UPDATE uporabnik 
                    SET vozovnica = %s, 
                    datum_veljavnosti = (SELECT (SELECT CURRENT_DATE + INTERVAL '%s day')::TIMESTAMP::DATE)
                    WHERE emso = '%s'""", [vrsta, velja, emso])
    conn.commit()

# nakupKarte(["1835012", 1])
#registracijaUporabnika(["000", "Kranj", "2022-02-02", "asdasdasd", "mailZaBednike", "123123123"] )

def prijava(uporabniskoIme, geslo):
    cur.execute(""" SELECT mail from uporabnik where mail = %s """, [uporabniskoIme])
    mailObstaja = cur.fetchall()
    
    if mailObstaja == []:
        return "Mail ne obstaja"

    
    cur.execute(""" SELECT geslo from uporabnik where mail = %s """, [uporabniskoIme])
    g = cur.fetchall()
    if g[0][0] == geslo:
        return True
    else: 
        return "Napačno geslo"

#podatki = ["8", "Alex", "08-08-2022", "Britof", "abcd@mail", "123123"]
#print(registracijaUporabnika(podatki))
#print(prijava("mailZaednike", "12313123"))