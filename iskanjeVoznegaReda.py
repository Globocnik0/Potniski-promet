import auth
from baze import *
from simulacijaPodatkov import *
import psycopg2, psycopg2.extensions, psycopg2.extras
from tabulate import tabulate

psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)

import csv


conn = psycopg2.connect(dbname = auth.db, host = auth.host, user = auth.user, password = auth.password)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

def poisciVozniRed(postaja1, postaja2): #dela sam ni tok fency. Pa nevem če dela.
    postaja1c = "'" + postaja1
    postaja1c += "'"
    postaja2c = "'" + postaja2
    postaja2c += "'"
    cur.execute( """ SELECT vlak, cas_prihoda, cas_odhoda, postaja.ime as postaja, postaja.id as postajaId, proga from voznired
                    join postaja on voznired.postaja = postaja.id
                    where postaja.ime = %s or postaja.ime = %s
                    order by proga, cas_prihoda""", [postaja1c, postaja2c])
    
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

#vrne začetno ter končno relacijo vendar v napačnem vrstnem redu glede na čas.
def poisciVozniRed2(p1, p2):
    cur.execute("""SELECT id FROM postaja WHERE ime = %s""", [p1])
    p11 = cur.fetchall()[0][0]
    cur.execute("""SELECT id FROM postaja WHERE ime = %s""", [p2])
    p22 = cur.fetchall()[0][0]
    
    cur.execute(""" SELECT p.ime, cas_odhoda, vr.proga FROM voznired vr
                JOIN
                    (SELECT pr2.proga 
                    FROM progekraji pr2
                    JOIN
                        (SELECT proga, zaporedna_st from progekraji 
                        WHERE postaja = %s
                        GROUP BY proga, zaporedna_st) pr1

                    ON pr2.proga = pr1.proga
                    WHERE pr2.postaja = %s AND pr2.zaporedna_st > pr1.zaporedna_st
                    GROUP BY pr2.proga)  pr

                ON pr.proga = vr.proga
                JOIN postaja p 
                ON p.id = vr.postaja
                WHERE vr.postaja = %s OR vr.postaja = %s""", [p11, p22, p11, p22])

    tabela = cur.fetchall()


    return tabela

#Isto kot zgoraj vendar v napačnem vrstem redu

def poisciVmesnePostaje(p1, p2):
    cur.execute("""SELECT id FROM postaja WHERE ime = %s""", [p1])
    p11 = cur.fetchall()[0][0]
    cur.execute("""SELECT id FROM postaja WHERE ime = %s""", [p2])
    p22 = cur.fetchall()[0][0]
    
    cur.execute(""" SELECT vr.postaja, po.ime, cas_odhoda, vr.proga, vr.voznja FROM voznired vr
                JOIN
                    (SELECT pr2.proga 
                    FROM progekraji pr2
                    JOIN
                        (SELECT proga, zaporedna_st from progekraji 
                        WHERE postaja = %s
                        GROUP BY proga, zaporedna_st) pr1

                    ON pr2.proga = pr1.proga
                    WHERE pr2.postaja = %s AND pr2.zaporedna_st > pr1.zaporedna_st
                    GROUP BY pr2.proga)  pr

                ON pr.proga = vr.proga
                --WHERE vr.postaja = %s OR vr.postaja = %s

            JOIN progekraji pk1 ON pk1.proga = vr.proga AND pk1.postaja= vr.postaja
            JOIN postaja po ON vr.postaja = po.id
            WHERE pk1.zaporedna_st >= (SELECT zaporedna_st FROM progekraji pk WHERE pk.proga = vr.proga AND pk.postaja = %s) 
            AND pk1.zaporedna_st <= (SELECT zaporedna_st FROM progekraji pk WHERE pk.proga = vr.proga AND pk.postaja = %s)
            ORDER BY vr.voznja, vr.proga, vr.cas_odhoda  ASC""", [p11, p22, p11, p22, p11, p22])

    tabela = cur.fetchall()

    return tabela

def razlicneProgeNaRelaciji(p1, p2): #poisce indexe prog ki povezujejo relaciji
    cur.execute("""SELECT id FROM postaja WHERE ime = %s""", [p1])
    p11 = cur.fetchall()[0][0]
    cur.execute("""SELECT id FROM postaja WHERE ime = %s""", [p2])
    p22 = cur.fetchall()[0][0]
    
    cur.execute(""" SELECT vr.proga FROM voznired vr
                JOIN
                    (SELECT pr2.proga 
                    FROM progekraji pr2
                    JOIN
                        (SELECT proga, zaporedna_st from progekraji 
                        WHERE postaja = %s
                        GROUP BY proga, zaporedna_st) pr1

                    ON pr2.proga = pr1.proga
                    WHERE pr2.postaja = %s AND pr2.zaporedna_st > pr1.zaporedna_st
                    GROUP BY pr2.proga)  pr

                ON pr.proga = vr.proga
                JOIN postaja p 
                ON p.id = vr.postaja
                WHERE vr.postaja = %s OR vr.postaja = %s
                GROUP BY vr.proga""", [p11, p22, p11, p22])
    

    tabela = cur.fetchall()
    return tabela

#vrne začetno in končno postajo v pravem časovnem zaporedju
def poisciVozniRed22(p1, p2): 
    cur.execute("""SELECT id FROM postaja WHERE ime = %s""", [p1])
    p11 = cur.fetchall()[0][0]
    cur.execute("""SELECT id FROM postaja WHERE ime = %s""", [p2])
    p22 = cur.fetchall()[0][0]
    
    cur.execute("""SELECT vr.postaja, po.ime, vr.cas_odhoda FROM voznired vr
                    JOIN
                        (SELECT pr2.proga 
                        FROM progekraji pr2
                        JOIN
                            (SELECT proga, zaporedna_st from progekraji 
                            WHERE postaja = %s
                            GROUP BY proga, zaporedna_st) pr1

                        ON pr2.proga = pr1.proga
                        WHERE pr2.postaja = %s AND pr2.zaporedna_st > pr1.zaporedna_st
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
                                        WHERE postaja = %s
                                        GROUP BY proga, zaporedna_st) pr11

                                    ON pr22.proga = pr11.proga
                                    WHERE pr22.postaja = %s AND pr22.zaporedna_st > pr11.zaporedna_st
                                    GROUP BY pr22.proga)  prr

                                ON prr.proga = vrr.proga

                JOIN progekraji pk11 ON pk11.proga = vrr.proga AND pk11.postaja= vrr.postaja
                WHERE pk11.zaporedna_st >= (SELECT zaporedna_st FROM progekraji pkk WHERE pkk.proga = vrr.proga AND pkk.postaja = %s) 
                AND pk11.zaporedna_st <= (SELECT zaporedna_st FROM progekraji pkk WHERE pkk.proga = vrr.proga AND pkk.postaja = %s) 
                AND vrr.postaja = %s) vr11
                    
                ON vr11.proga = vr.proga AND vr11.voznja = vr.voznja
                    WHERE (vr.postaja = %s OR vr.postaja = %s)
                    ORDER BY vr11.cas_odhoda, zaporedna_st""", [p11, p22, p11, p22, p11, p22, p11, p11, p22])

    tabela = cur.fetchall()
    return tabela

def vozniRedZacetnaKoncna(vstopna, iztopna):
    cur.execute("""SELECT * from vozniRedZacetnaKoncna(%s, %s)""", [vstopna, iztopna])
    tabela = cur.fetchall()
    return tabela

def poisciVozniRed3(p1, p2): #Vrne vozni red med dvema krajema z vmesnimi kraji s pravilnim časovnim zaporedjem
    cur.execute("""SELECT id FROM postaja WHERE ime = %s""", [p1])
    p11 = cur.fetchall()[0][0]
    cur.execute("""SELECT id FROM postaja WHERE ime = %s""", [p2])
    p22 = cur.fetchall()[0][0]
    print(p11, p22)
    cur.execute("""SELECT vr.postaja, po.ime, vr.cas_odhoda FROM voznired vr
                    JOIN
                        (SELECT pr2.proga 
                        FROM progekraji pr2
                        JOIN
                            (SELECT proga, zaporedna_st from progekraji 
                            WHERE postaja = %s
                            GROUP BY proga, zaporedna_st) pr1

                        ON pr2.proga = pr1.proga
                        WHERE pr2.postaja = %s AND pr2.zaporedna_st > pr1.zaporedna_st
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
                                        WHERE postaja = %s
                                        GROUP BY proga, zaporedna_st) pr11

                                    ON pr22.proga = pr11.proga
                                    WHERE pr22.postaja = %s AND pr22.zaporedna_st > pr11.zaporedna_st
                                    GROUP BY pr22.proga)  prr

                                ON prr.proga = vrr.proga

                JOIN progekraji pk11 ON pk11.proga = vrr.proga AND pk11.postaja= vrr.postaja
                WHERE pk11.zaporedna_st >= (SELECT zaporedna_st FROM progekraji pkk WHERE pkk.proga = vrr.proga AND pkk.postaja = %s) 
                AND pk11.zaporedna_st <= (SELECT zaporedna_st FROM progekraji pkk WHERE pkk.proga = vrr.proga AND pkk.postaja = %s) 
                AND vrr.postaja = %s) vr11
                    
                ON vr11.proga = vr.proga AND vr11.voznja = vr.voznja
                    WHERE pk1.zaporedna_st <= (SELECT zaporedna_st FROM progekraji pk WHERE pk.proga = vr.proga AND pk.postaja = %s)
                    AND pk1.zaporedna_st >= (SELECT zaporedna_st FROM progekraji pk WHERE pk.proga = vr.proga AND pk.postaja = %s) 
                    ORDER BY vr11.cas_odhoda, zaporedna_st""", [p11, p22, p11, p22, p11, p22, p11, p22, p11])

    tabela = cur.fetchall()
    return tabela

def vozniRed333(vstopna, iztopna):
    cur.execute("""SELECT * from dobiVozniRed3(%s, %s)""", [vstopna, iztopna])
    tabela = cur.fetchall()
    return tabela

#Nevem točno že kaj dela ampak je potrebna v funkciji vozniRedVGrupah
def vrstniRedProgaVoznja(p1, p2):
    cur.execute("""SELECT id FROM postaja WHERE ime = %s""", [p1])
    p11 = cur.fetchall()[0][0]
    cur.execute("""SELECT id FROM postaja WHERE ime = %s""", [p2])
    p22 = cur.fetchall()[0][0]
    
        
    cur.execute("""SELECT vr.proga, vr.voznja FROM voznired vr
                JOIN
                    (SELECT pr2.proga 
                    FROM progekraji pr2
                    JOIN
                        (SELECT proga, zaporedna_st from progekraji 
                        WHERE postaja = %s
                        GROUP BY proga, zaporedna_st) pr1

                    ON pr2.proga = pr1.proga
                    WHERE pr2.postaja = %s AND pr2.zaporedna_st > pr1.zaporedna_st
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
                                        WHERE postaja = %s
                                        GROUP BY proga, zaporedna_st) pr11

                                    ON pr22.proga = pr11.proga
                                    WHERE pr22.postaja = %s AND pr22.zaporedna_st > pr11.zaporedna_st
                                    GROUP BY pr22.proga)  prr

                                ON prr.proga = vrr.proga

                            JOIN progekraji pk11 ON pk11.proga = vrr.proga AND pk11.postaja= vrr.postaja
                            WHERE pk11.zaporedna_st >= (SELECT zaporedna_st FROM progekraji pkk WHERE pkk.proga = vrr.proga AND pkk.postaja = %s) 
                            AND pk11.zaporedna_st <= (SELECT zaporedna_st FROM progekraji pkk WHERE pkk.proga = vrr.proga AND pkk.postaja = %s) 
                            AND vrr.postaja = %s) vr11
                    
                ON vr11.proga = vr.proga AND vr11.voznja = vr.voznja
                WHERE pk1.zaporedna_st <= (SELECT zaporedna_st FROM progekraji pk WHERE pk.proga = vr.proga AND pk.postaja = %s)
                    AND pk1.zaporedna_st >= (SELECT zaporedna_st FROM progekraji pk WHERE pk.proga = vr.proga AND pk.postaja = %s) 
                    
                GROUP BY vr.proga, vr.voznja, vr11.cas_odhoda
                ORDER BY vr11.cas_odhoda""", [p11, p22, p11, p22, p11, p22, p11, p22, p11])

    tabela = cur.fetchall()
    return tabela

#Vrne seznam vseh vozenj urejenih po času z vmesnimi postajami
def vozniRedVGrupah(p1, p2):
    cur.execute("""SELECT id FROM postaja WHERE ime = %s""", [p1])
    p11 = cur.fetchall()[0][0]
    cur.execute("""SELECT id FROM postaja WHERE ime = %s""", [p2])
    p22 = cur.fetchall()[0][0]
    
    progaVoznja = vrstniRedProgaVoznja(p1, p2)
    grupe = []
    for i, j in progaVoznja:
        cur.execute("""SELECT vr.postaja, po.ime, vr.cas_odhoda FROM voznired vr
                        JOIN
                            (SELECT pr2.proga 
                            FROM progekraji pr2
                            JOIN
                                (SELECT proga, zaporedna_st from progekraji 
                                WHERE postaja = %s
                                GROUP BY proga, zaporedna_st) pr1

                            ON pr2.proga = pr1.proga
                            WHERE pr2.postaja = %s AND pr2.zaporedna_st > pr1.zaporedna_st
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
                                            WHERE postaja = %s
                                            GROUP BY proga, zaporedna_st) pr11

                                        ON pr22.proga = pr11.proga
                                        WHERE pr22.postaja = %s AND pr22.zaporedna_st > pr11.zaporedna_st
                                        GROUP BY pr22.proga)  prr

                                    ON prr.proga = vrr.proga

                    JOIN progekraji pk11 ON pk11.proga = vrr.proga AND pk11.postaja= vrr.postaja
                    WHERE pk11.zaporedna_st >= (SELECT zaporedna_st FROM progekraji pkk WHERE pkk.proga = vrr.proga AND pkk.postaja = %s) 
                    AND pk11.zaporedna_st <= (SELECT zaporedna_st FROM progekraji pkk WHERE pkk.proga = vrr.proga AND pkk.postaja = %s) 
                    AND vrr.postaja = %s) vr11
                        
                    ON vr11.proga = vr.proga AND vr11.voznja = vr.voznja
                        WHERE pk1.zaporedna_st <= (SELECT zaporedna_st FROM progekraji pk WHERE pk.proga = vr.proga AND pk.postaja = %s)
                        AND pk1.zaporedna_st >= (SELECT zaporedna_st FROM progekraji pk WHERE pk.proga = vr.proga AND pk.postaja = %s) 
                        AND vr.proga = %s 
                        AND vr.voznja = %s
                        ORDER BY vr11.cas_odhoda, zaporedna_st""", [p11, p22, p11, p22, p11, p22, p11, p22, p11, i, j])   

        tabela = cur.fetchall()
        grupe.append(tabela)
    return grupe


#tabela = vozniRedZacetnaKoncna("Kranj", "Ljubljana")

