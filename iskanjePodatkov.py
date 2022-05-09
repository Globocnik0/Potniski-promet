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
    
    komanda = """ SELECT vr.postaja, po.ime, cas_odhoda, vr.proga, vr.voznja FROM voznired vr
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

            JOIN progekraji pk1 ON pk1.proga = vr.proga AND pk1.postaja= vr.postaja
            JOIN postaja po ON vr.postaja = po.id
            WHERE pk1.zaporedna_st >= (SELECT zaporedna_st FROM progekraji pk WHERE pk.proga = vr.proga AND pk.postaja = {}) 
            AND pk1.zaporedna_st <= (SELECT zaporedna_st FROM progekraji pk WHERE pk.proga = vr.proga AND pk.postaja = {})
            ORDER BY vr.voznja, vr.proga, vr.cas_odhoda  ASC""".format(p11, p22, p11, p22, p11, p22)

    cur.execute(komanda)
    tabela = cur.fetchall()

    return tabela

def razlicneProgeNaRelaciji(p1, p2): #poisce indexe prog ki povezujejo relaciji
    cur.execute("""SELECT id FROM postaja WHERE ime = '{}'""".format(p1))
    p11 = cur.fetchall()[0][0]
    cur.execute("""SELECT id FROM postaja WHERE ime = '{}'""".format(p2))
    p22 = cur.fetchall()[0][0]
    
    komanda = """ SELECT vr.proga FROM voznired vr
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
                WHERE vr.postaja = {} OR vr.postaja = {}
                GROUP BY vr.proga""".format(p11, p22, p11, p22)
    
    cur.execute(komanda)
    tabela = cur.fetchall()
    return tabela

def poisciVozniRed3(p1, p2): #vsako voznjo med dvema krajema zapakira v svoj seznam.
    cur.execute("""SELECT id FROM postaja WHERE ime = '{}'""".format(p1))
    p11 = cur.fetchall()[0][0]
    cur.execute("""SELECT id FROM postaja WHERE ime = '{}'""".format(p2))
    p22 = cur.fetchall()[0][0]
    
    komanda = """SELECT vr.postaja, po.ime, vr.cas_odhoda FROM voznired vr
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

                JOIN progekraji pk1 ON pk1.proga = vr.proga AND pk1.postaja= vr.postaja
                JOIN postaja po ON vr.postaja = po.id

                JOIN
                (
                SELECT vrr.postaja, vrr.cas_odhoda, vrr.proga, vrr.voznja FROM voznired vrr
                                JOIN
                                    (SELECT pr22.proga 
                                    FROM progekraji pr22
                                    JOIN
                                        (SELECT proga, zaporedna_st from progekraji 
                                        WHERE postaja = {}
                                        GROUP BY proga, zaporedna_st) pr11

                                    ON pr22.proga = pr11.proga
                                    WHERE pr22.postaja = {} AND pr22.zaporedna_st > pr11.zaporedna_st
                                    GROUP BY pr22.proga)  prr

                                ON prr.proga = vrr.proga

                JOIN progekraji pk11 ON pk11.proga = vrr.proga AND pk11.postaja= vrr.postaja
                WHERE pk11.zaporedna_st >= (SELECT zaporedna_st FROM progekraji pkk WHERE pkk.proga = vrr.proga AND pkk.postaja = {}) 
                AND pk11.zaporedna_st <= (SELECT zaporedna_st FROM progekraji pkk WHERE pkk.proga = vrr.proga AND pkk.postaja = {}) 
                AND vrr.postaja = {}) vr11
                    
                ON vr11.proga = vr.proga AND vr11.voznja = vr.voznja
                    WHERE pk1.zaporedna_st <= (SELECT zaporedna_st FROM progekraji pk WHERE pk.proga = vr.proga AND pk.postaja = {})
                    AND pk1.zaporedna_st >= (SELECT zaporedna_st FROM progekraji pk WHERE pk.proga = vr.proga AND pk.postaja = {}) 
                    ORDER BY vr11.cas_odhoda, zaporedna_st""".format(p11, p22, p11, p22, p11, p22, p11, p22, p11)   

    cur.execute(komanda)
    tabela = cur.fetchall()
    return tabela

def vrstniRedProgaVoznja(p1, p2):
    cur.execute("""SELECT id FROM postaja WHERE ime = '{}'""".format(p1))
    p11 = cur.fetchall()[0][0]
    cur.execute("""SELECT id FROM postaja WHERE ime = '{}'""".format(p2))
    p22 = cur.fetchall()[0][0]
    
    komanda = """SELECT vr.proga, vr.voznja FROM voznired vr
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

                JOIN progekraji pk1 ON pk1.proga = vr.proga AND pk1.postaja= vr.postaja
                JOIN postaja po ON vr.postaja = po.id

                JOIN
                (
                SELECT vrr.postaja, vrr.cas_odhoda, vrr.proga, vrr.voznja FROM voznired vrr
                                JOIN
                                    (SELECT pr22.proga 
                                    FROM progekraji pr22
                                    JOIN
                                        (SELECT proga, zaporedna_st from progekraji 
                                        WHERE postaja = {}
                                        GROUP BY proga, zaporedna_st) pr11

                                    ON pr22.proga = pr11.proga
                                    WHERE pr22.postaja = {} AND pr22.zaporedna_st > pr11.zaporedna_st
                                    GROUP BY pr22.proga)  prr

                                ON prr.proga = vrr.proga

                            JOIN progekraji pk11 ON pk11.proga = vrr.proga AND pk11.postaja= vrr.postaja
                            WHERE pk11.zaporedna_st >= (SELECT zaporedna_st FROM progekraji pkk WHERE pkk.proga = vrr.proga AND pkk.postaja = {}) 
                            AND pk11.zaporedna_st <= (SELECT zaporedna_st FROM progekraji pkk WHERE pkk.proga = vrr.proga AND pkk.postaja = {}) 
                            AND vrr.postaja = {}) vr11
                    
                ON vr11.proga = vr.proga AND vr11.voznja = vr.voznja
                WHERE pk1.zaporedna_st <= (SELECT zaporedna_st FROM progekraji pk WHERE pk.proga = vr.proga AND pk.postaja = {})
                    AND pk1.zaporedna_st >= (SELECT zaporedna_st FROM progekraji pk WHERE pk.proga = vr.proga AND pk.postaja = {}) 
                    
                GROUP BY vr.proga, vr.voznja, vr11.cas_odhoda
                ORDER BY vr11.cas_odhoda""".format(p11, p22, p11, p22, p11, p22, p11, p22, p11)
    
    cur.execute(komanda)
    tabela = cur.fetchall()
    return tabela

def vozniRedVGrupah(p1, p2):
    cur.execute("""SELECT id FROM postaja WHERE ime = '{}'""".format(p1))
    p11 = cur.fetchall()[0][0]
    cur.execute("""SELECT id FROM postaja WHERE ime = '{}'""".format(p2))
    p22 = cur.fetchall()[0][0]
    
    progaVoznja = vrstniRedProgaVoznja(p1, p2)
    grupe = []
    for i, j in progaVoznja:
        komanda = """SELECT vr.postaja, po.ime, vr.cas_odhoda FROM voznired vr
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

                    JOIN progekraji pk1 ON pk1.proga = vr.proga AND pk1.postaja= vr.postaja
                    JOIN postaja po ON vr.postaja = po.id

                    JOIN
                    (
                    SELECT vrr.postaja, vrr.cas_odhoda, vrr.proga, vrr.voznja FROM voznired vrr
                                    JOIN
                                        (SELECT pr22.proga 
                                        FROM progekraji pr22
                                        JOIN
                                            (SELECT proga, zaporedna_st from progekraji 
                                            WHERE postaja = {}
                                            GROUP BY proga, zaporedna_st) pr11

                                        ON pr22.proga = pr11.proga
                                        WHERE pr22.postaja = {} AND pr22.zaporedna_st > pr11.zaporedna_st
                                        GROUP BY pr22.proga)  prr

                                    ON prr.proga = vrr.proga

                    JOIN progekraji pk11 ON pk11.proga = vrr.proga AND pk11.postaja= vrr.postaja
                    WHERE pk11.zaporedna_st >= (SELECT zaporedna_st FROM progekraji pkk WHERE pkk.proga = vrr.proga AND pkk.postaja = {}) 
                    AND pk11.zaporedna_st <= (SELECT zaporedna_st FROM progekraji pkk WHERE pkk.proga = vrr.proga AND pkk.postaja = {}) 
                    AND vrr.postaja = {}) vr11
                        
                    ON vr11.proga = vr.proga AND vr11.voznja = vr.voznja
                        WHERE pk1.zaporedna_st <= (SELECT zaporedna_st FROM progekraji pk WHERE pk.proga = vr.proga AND pk.postaja = {})
                        AND pk1.zaporedna_st >= (SELECT zaporedna_st FROM progekraji pk WHERE pk.proga = vr.proga AND pk.postaja = {}) 
                        AND vr.proga = {} 
                        AND vr.voznja = {}
                        ORDER BY vr11.cas_odhoda, zaporedna_st""".format(p11, p22, p11, p22, p11, p22, p11, p22, p11, i, j)   

        cur.execute(komanda)
        tabela = cur.fetchall()
        grupe.append(tabela)
    return grupe

def registracijaUporabnika(podatki): #podatki so [emso, ime, rojstvo, naslov, mail, geslo]
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
        
def nakupKarte(podatki): #[emso, vrsta Karte]
    
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
for tab in vozniRedVGrupah("Ljubljana", "Kranj"):
    print(tabulate(tab))

