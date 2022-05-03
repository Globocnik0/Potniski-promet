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
    komanda = """ SELECT postaja, cas_odhoda, vr.proga FROM voznired vr
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
                WHERE vr.postaja = {} OR vr.postaja = {}""".format(p1, p2, p1, p2)
    
    cur.execute(komanda)
    tabela = cur.fetchall()


    return tabela

tabela = poisciVozniRed2(2, 4)
h = ["Postaja", "cas_odhoda", "vlak", "proga"]
print(tabulate(tabela))