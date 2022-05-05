import auth
from baze import *
from simulacijaPodatkov import *
import psycopg2, psycopg2.extensions, psycopg2.extras
from tabulate import tabulate

psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)

import csv


conn = psycopg2.connect(dbname = auth.db, host = auth.host, user = auth.user, password = auth.password)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

def poisciVozniRed(postaja1, postaja2):
    postaja1c = "'" + postaja1
    postaja1c += "'"
    postaja2c = "'" + postaja2
    postaja2c += "'"
    komanda = """ SELECT vlak, cas_prihoda, cas_odhoda, postaja.ime as postaja, postaja.id as postajaId, proga from voznired
                    join postaja on voznired.postaja = postaja.id
                    where postaja.ime = {} or postaja.ime = {}
                    order by proga, cas_prihoda""".format(postaja1c, postaja2c)

    cur.execute(komanda)
    tabela = cur.fetchall()
    vrni = []
    print("dolžinaTabelePrej", len(tabela))
    zaOdstranit = []
    i = 0
    while(i < len(tabela)-1):
        po1= tabela[i][3]
        po2 = tabela[i+1][3]

        pr1 = tabela[i][5]
        pr2 = tabela[i+1][5]

        print(po1, postaja1,)
        print(po2, postaja2)
        if ((po1 == postaja1 and po2 == postaja2) and (pr1 == pr2)):
            vrni.append(tabela[i])
            vrni.append(tabela[i+1])
            i += 1
        i+=1

    print("dolžinaTabelePotem", len(vrni))
    return vrni

def poisciVozniRed2(p1, p2):
    cur.execute("""SELECT id FROM postaja WHERE ime = '{}'""".format(p1))
    p11 = cur.fetchall()[0][0]
    cur.execute("""SELECT id FROM postaja WHERE ime = '{}'""".format(p2))
    p22 = cur.fetchall()[0][0]
    
    komanda = """ SELECT p.ime, cas_odhoda FROM voznired vr
                JOIN
                    (SELECT pr2.proga 
                    FROM progekraji pr2
                    JOIN
                        (SELECT proga, zaporedna_st from progekraji 
                        WHERE postaja = {}
                        GROUP BY proga, zaporedna_st) pr1

                    ON pr2.proga = pr1.proga
                    WHERE pr2.postaja = {} AND pr2.zaporedna_st > pr1.zaporedna_st
                    GROUP BY pr2.proga)  pr

                ON pr.proga = vr.proga
                JOIN postaja p 
                ON p.id = vr.postaja
                WHERE vr.postaja = {} OR vr.postaja = {}""".format(p11, p22, p11, p22)
    
    cur.execute(komanda)
    tabela = cur.fetchall()


    return tabela

#iskanje vmesnih postaj

def poisciVmesnePostaje(p1, p2):
    cur.execute("""SELECT id FROM postaja WHERE ime = '{}'""".format(p1))
    p11 = cur.fetchall()[0][0]
    cur.execute("""SELECT id FROM postaja WHERE ime = '{}'""".format(p2))
    p22 = cur.fetchall()[0][0]
    
    komanda = """ SELECT vr.postaja, cas_odhoda, vr.proga FROM voznired vr
                JOIN
                    (SELECT pr2.proga 
                    FROM progekraji pr2
                    JOIN
                        (SELECT proga, zaporedna_st from progekraji 
                        WHERE postaja = {}
                        GROUP BY proga, zaporedna_st) pr1

                    ON pr2.proga = pr1.proga
                    WHERE pr2.postaja = {} AND pr2.zaporedna_st > pr1.zaporedna_st
                    GROUP BY pr2.proga)  pr

                ON pr.proga = vr.proga
                --WHERE vr.postaja = {} OR vr.postaja = {}

            JOIN progekraji p ON p.proga = vr.proga AND p.postaja= vr.postaja
            WHERE p.zaporedna_st >= (SELECT zaporedna_st FROM progekraji pk WHERE pk.proga = vr.proga AND pk.postaja = {}) 
            AND p.zaporedna_st <= (SELECT zaporedna_st FROM progekraji pk WHERE pk.proga = vr.proga AND pk.postaja = {})""".format(p11, p22, p11, p22, p11, p22)

    cur.execute(komanda)
    tabela = cur.fetchall()

    return tabela

def registracijaUporabnika(podatki): #podatki so emso, ime, rojstvo, naslov, mail, geslo
    cur.execute(""" SELECT mail from potnik where mail = '{}' """.format(podatki[4]))
    mailObstaja = cur.fetchall()
    if mailObstaja:
        print("mail obstaja. Not cool maaaaaannnn.")
        return

    cur.execute(""" SELECT emso from potnik where emso = '{}' """.format(podatki[0]))
    emsoObstaja = cur.fetchall()
    if emsoObstaja:
        print("Obstajaš. Not cool maaaannnnnn.")
        return

    cur.execute("""INSERT INTO potnik(emso, ime, rojstvo, naslov, mail, geslo) values (%s, %s, %s, %s, %s, %s)""", podatki)
    conn.commit()
        
def nakupKarte(podatki): #emso, vrsta Karte
    
    emso = podatki[0]
    vrsta = podatki[1]
    cur.execute("""SELECT velja FROM vozovnica WHERE id = {} """.format(vrsta))
    velja = cur.fetchall()[0][0]
    cur.execute(""" UPDATE potnik 
                    SET vozovnica = {}, 
                    datum_veljavnosti = (SELECT (SELECT CURRENT_DATE + INTERVAL '{} day')::TIMESTAMP::DATE)
                    WHERE emso = '{}'""".format(vrsta, velja, emso))
    conn.commit()

# nakupKarte(["1835012", 1])
tabela = poisciVozniRed2("Ljubljana", "Kranj")
print(tabulate(tabela))