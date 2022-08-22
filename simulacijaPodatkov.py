import random
from turtle import st
import exrex as ex
import auth_public as auth
import numpy as np
import psycopg2, psycopg2.extensions, psycopg2.extras
import podatkiZaGeneracijo as pzg
from faker import Faker
import cas

fake = Faker()
def transponiraj(a1, a2):
    vnos = np.array([a1, a2])
    vnos = np.transpose(vnos)
    return vnos

def transponiraj2(a):
    vnos = np.transpose(a)
    return vnos


#----MODEL---------

def napolniTabeloModel(cur):
    capList = [50, 100, 150, 200, 300]
    tezaList = [10, 12, 20, 20, 23]
    imeList = ["taHitr", "taPocasn", "taVelik", "zaKolo", "zaPivoInCvetje"]
    vnosModel = transponiraj2([capList, tezaList, imeList])
    komanda = """INSERT INTO model(kapaciteta, teza, ime) values"""
    for val in vnosModel:
        niz = "({}, {}, '{}'),".format(val[0], val[1], val[2])
        komanda += niz
    cur.execute(komanda[:-1])
    

#----VLAK----------------
def napolniTabeloVlak(cur, stVnosov):
    cur.execute(""" SELECT id from model""")
    modeliNaVoljo = cur.fetchall()
    letaIzdelava = [random.randint(1980, 2020) for m in range(stVnosov)]
    modeli = [modeliNaVoljo[random.randint(0, len(modeliNaVoljo)-1)][0] for m in range(stVnosov)]
    vnosVlak = transponiraj(letaIzdelava, modeli)

    komanda = """INSERT INTO vlak(leto_izdelave, model) values"""
    for val in vnosVlak:
        niz = "({}, {}),".format(val[0], val[1])
        komanda += niz
    cur.execute(komanda[:-1])
    

#-----POSTAJA------------------------------------------------
def napolniTabeloPostaja( cur):
    komanda = """INSERT INTO postaja(ime) values"""
    for val in pzg.imenaPostaj:
        niz = "({}),".format(val)
        komanda += niz
    cur.execute(komanda[:-1])
     #znebimo se zadnje vejice    

#---------------ZAPOSLENI------------------------------------------------
def napolniTabeloZaposleni( cur,stVnosov):
    komanda = """INSERT INTO zaposlen(emso, ime, rojstvo, naslov, datum_zaposlitve, naziv) values"""
    emsos = [random.randint(1000000, 9999999) for m in range(stVnosov)]
    imens = [pzg.imena[random.randint(0, len(pzg.imena)-1)] for m in range(stVnosov)]
    primks = [pzg.priimki[random.randint(0, len(pzg.priimki)-1)] for m in range(stVnosov)]
    rojstva = [(random.randint(1, 28), random.randint(1, 12), random.randint(1960, 2000)) for m in range(stVnosov)]
    naslovi = [pzg.naselja[random.randint(0, len(pzg.naselja)-1)] for m in range(stVnosov)]
    stevilke = [random.randint(0, 1000) for m in range(stVnosov)]
    zaposlitve = [(random.randint(1, 28), random.randint(1, 12), random.randint(1980, 2020)) for m in range(stVnosov)]
    nazivs = [pzg.nazivi[random.randint(0,len(pzg.nazivi)-1)] for m in range(stVnosov)]
    list = np.array([emsos, imens, primks, rojstva, naslovi, stevilke, zaposlitve, nazivs])
    vnosZaposleni = transponiraj2(list)
    
    for val in vnosZaposleni:
        em = val[0]
        im = val[1] + " " + val[2]
        im = im.replace("' '", " ")
        d = datum(val[3])
        nas = val[4] + " " + str(val[5])
        nas = nas.replace("' ", " ") + "'"
        dz = datum(val[6])
        niz = "('{}', {}, {}, {}, {}, {}),".format(em, im, d, nas, dz, val[7])
        komanda += niz
    cur.execute(komanda[:-1])
           

#-----------PREGLED------------------
def napolniTabeloPregled(cur, stVnosov):
    komanda = """INSERT INTO pregled(vlak, zaposleni, datum_pregleda, komentar) values"""
    
    cur.execute(""" SELECT id from vlak""")
    vlakiNaVoljo = cur.fetchall()
    vlaki = [vlakiNaVoljo[random.randint(0, len(vlakiNaVoljo)-1)][0] for m in range(stVnosov)]

    cur.execute("""SELECT emso from zaposlen""")
    zaposleniNaVoljo = cur.fetchall()
    zaposleni = [zaposleniNaVoljo[random.randint(0, len(zaposleniNaVoljo)-1)][0] for m in range(stVnosov)]

    datums = [(random.randint(1, 28), random.randint(1, 12), random.randint(1990, 2022)) for m in range(stVnosov)]

    koments = [pzg.komentarji[m%(len(pzg.komentarji)-1)] for m in range(stVnosov)]

    list = np.array([vlaki, zaposleni, datums, koments])
    vnosPregledi= transponiraj2(list)

    for val in vnosPregledi:
        vl = val[0]
        zap = val[1]
        dat = datum(val[2])
        kom = val[3]
        niz = "({}, {}, {}, {}),".format(vl, zap, dat, kom)
        komanda += niz
    cur.execute(komanda[:-1])
           

#-----------VOZOVNICA-----------------  
def napolniTabeloVozovnica(cur):
    komanda = """INSERT INTO vozovnica(id, ime, cas_veljavnost, cena, opis) values"""
    
    list = np.array([pzg.vozovnicaId ,pzg.vozovnicaIme, pzg.vozovnicaVelja, pzg.vozovnicaCena, pzg.vozovnicaOpis])
    vnosVozovnice= transponiraj2(list)

    for val in vnosVozovnice:
        id = val[0]
        im = val[1]
        cen = val[2]
        vel = val[3]
        op = val[4]
        niz = "({}, {}, {}, {}, {}),".format(id, im, cen, vel, op)
        komanda += niz
    cur.execute(komanda[:-1])
    

#---------POTNIKI------------------
def napolniTabeloPotnik(cur, stVnosov):
    komanda = """INSERT INTO potnik(emso, ime, rojstvo, naslov, mail, geslo, vozovnica, datum_veljavnosti) values"""
    cur.execute(""" SELECT id from vozovnica""")
    vozIds = cur.fetchall()
    
    emsos = [random.randint(1000000, 9999999) for m in range(stVnosov)]
    emsos = list(set(emsos))
    stVnosov = len(emsos)
    imens = [pzg.imena[random.randint(0, len(pzg.imena)-1)] for m in range(stVnosov)]
    primks = [pzg.priimki[random.randint(0, len(pzg.priimki)-1)] for m in range(stVnosov)]
    rojstvs = [(random.randint(1, 28), random.randint(1, 12), random.randint(1960, 2000)) for m in range(stVnosov)]
    naslovs = [pzg.naselja[random.randint(0, len(pzg.naselja)-1)] for m in range(stVnosov)]
    stevilks = [random.randint(0, 1000) for m in range(stVnosov)]
    vozovnicas = [vozIds[random.randint(0, len(vozIds)-1)][0] for m in range(stVnosov)]
    datumis = [(random.randint(1, 28), random.randint(1, 12), random.randint(2021, 2022)) for m in range(stVnosov)]
    llist = np.array([emsos, imens, primks, rojstvs, naslovs, stevilks, vozovnicas, datumis])
    vnosPotniki = transponiraj2(llist)
    
    for i, val in enumerate(vnosPotniki):
        em = val[0]
        ime = val[1].replace("'", "")
        priimk = val[2].replace("'", "")
        imPr = "'" + ime + " " + priimk + "'"
        d = datum(val[3])
        nas = val[4] + " " + str(val[5])
        nas = nas.replace("' ", " ") + "'"
        ma = "'" + ime + "." + priimk + str(i) + "@gmail.com" + "'"
        ges = "'123'"
        voz = val[6]
        dat = datum(val[7])
        niz = "('{}', {}, {}, {}, {}, {}, {}, {}),".format(em, imPr, d, nas, ma, ges, voz, dat)
        komanda += niz
    cur.execute(komanda[:-1])
    
#----UPORABNIK-------

def napolniTabeloUporabnik(cur, stVnosovPotnik, stVnosovZaposleni):
    komanda = """INSERT INTO uporabnik(emso, ime, rojstvo, naslov, naziv, vozovnica, datum_veljavnosti, mail, geslo) values"""
    cur.execute(""" SELECT id from vozovnica""")
    vozIds = cur.fetchall()
    
    emsos = [random.randint(1000000, 9000000) for m in range(stVnosovPotnik)]
    emsos = list(set(emsos))
    stVnosovPotnik = len(emsos)
    imens = [pzg.imena[random.randint(0, len(pzg.imena)-1)] for m in range(stVnosovPotnik)]
    primks = [pzg.priimki[random.randint(0, len(pzg.priimki)-1)] for m in range(stVnosovPotnik)]
    rojstvs = [(random.randint(1, 28), random.randint(1, 12), random.randint(1960, 2000)) for m in range(stVnosovPotnik)]
    naslovs = [pzg.naselja[random.randint(0, len(pzg.naselja)-1)] for m in range(stVnosovPotnik)]
    stevilks = [random.randint(0, 1000) for m in range(stVnosovPotnik)]
    nazivs = ["potnik" for m in range(stVnosovPotnik)]
    vozovnicas = [vozIds[random.randint(0, len(vozIds)-2)][0] for m in range(stVnosovPotnik)]
    datumis = [(random.randint(1, 28), random.randint(1, 12), random.randint(2021, 2022)) for m in range(stVnosovPotnik)]
    llist = np.array([emsos, imens, primks, rojstvs, naslovs, stevilks, nazivs, vozovnicas, datumis])
    vnosPotniki = transponiraj2(llist)
    
    for i, val in enumerate(vnosPotniki):
        em = val[0]
        ime = val[1].replace("'", "")
        priimk = val[2].replace("'", "")
        imPr = "'" + ime + " " + priimk + "'"
        d = datum(val[3])
        nas = val[4] + " " + str(val[5])
        nas = nas.replace("' ", " ") + "'"
        na = "'" + val[6] + "'"
        ma = "'" + ime + "." + priimk + str(i) + "@gmail.com" + "'"
        ges = "'123'"
        voz = val[7]
        dat = datum(val[8])
        niz = "('{}', {}, {}, {}, {}, {}, {}, {}, {}),".format(em, imPr, d, nas, na, voz, dat, ma, ges)
        komanda += niz
    cur.execute(komanda[:-1])

    komanda = """INSERT INTO uporabnik(emso, ime, rojstvo, naslov, naziv, vozovnica, datum_veljavnosti, mail, geslo) values"""
    cur.execute(""" SELECT id from vozovnica""")
    vozIds = cur.fetchall()
    
    emsos = [random.randint(9000001, 9999999) for m in range(stVnosovZaposleni)]
    emsos = list(set(emsos))
    stVnosovZaposleni = len(emsos)
    imens = [pzg.imena[random.randint(0, len(pzg.imena)-1)] for m in range(stVnosovZaposleni)]
    primks = [pzg.priimki[random.randint(0, len(pzg.priimki)-1)] for m in range(stVnosovZaposleni)]
    rojstvs = [(random.randint(1, 28), random.randint(1, 12), random.randint(1960, 2000)) for m in range(stVnosovZaposleni)]
    naslovs = [pzg.naselja[random.randint(0, len(pzg.naselja)-1)] for m in range(stVnosovZaposleni)]
    stevilks = [random.randint(0, 1000) for m in range(stVnosovZaposleni)]
    nazivs = [pzg.nazivi[random.randint(0,len(pzg.nazivi)-1)] for m in range(stVnosovZaposleni)]
    vozovnicas = [4 for m in range(stVnosovZaposleni)]
    datumis = [(random.randint(1, 28), random.randint(1, 12), random.randint(2021, 2022)) for m in range(stVnosovZaposleni)]
    llist = np.array([emsos, imens, primks, rojstvs, naslovs, stevilks, nazivs, vozovnicas, datumis])
    vnosPotniki = transponiraj2(llist)
    
    for i, val in enumerate(vnosPotniki):
        em = val[0]
        ime = val[1].replace("'", "")
        priimk = val[2].replace("'", "")
        imPr = "'" + ime + " " + priimk + "'"
        d = datum(val[3])
        nas = val[4] + " " + str(val[5])
        nas = nas.replace("' ", " ") + "'"
        na = val[6]
        ma = "'" + ime + "." + priimk + str(i) + "@vozna.slo" + "'"
        ges = "'123'"
        voz = val[7]
        dat = datum(val[8])
        niz = "('{}', {}, {}, {}, {}, {}, {}, {}, {}),".format(em, imPr, d, nas, na, voz, dat, ma, ges)
        komanda += niz
    cur.execute(komanda[:-1])

#------PROGA------------------
def napolniTabeloProga(cur):
    komanda = """INSERT INTO proga(id, seznam_postaj, razdalje) values"""
    
    pro = []
    razdalje = []
    for i, pr in enumerate(pzg.proge):
        pro.append(pr[::-1])
        razdalje.append(pzg.razdalje[i][::-1])    
    #dodal proge v nasprotno smer
    pzg.proge = pzg.proge + pro
    pzg.razdalje = pzg.razdalje + razdalje
    ids = np.arange(0, len(pzg.proge)) + 1
    progs = []
    razs = []
    for i, proga in enumerate(pzg.proge):
        pro = []
        razdalje = []
        razdalja = pzg.razdalje[i]
        razdalja.append(0)
        for j, p in enumerate(proga):
            p = p.replace("'", "")
            pro.append(p)
            razdalje.append(str(razdalja[j]))
        proStr = ",".join(pro)
        razStr = ",".join(razdalje)
        progs.append(proStr)
        razs.append(razStr)
    llist = np.array([ids, progs, razs])
    vnosProge = transponiraj2(llist)
    for val in vnosProge:
        id = val[0]
        sezP = val[1]
        sezRaz = val[2]
        niz = "({0}, '{1}', '{2}'),".format(id, sezP, sezRaz)
        komanda += niz
    cur.execute(komanda[:-1])
    

#----PROGA2------------------
def napolniTabeloProgeKraji(cur):
    cur.execute("""SELECT * FROM proga""")
    prIds, prStr, prRaz = np.transpose(np.array(cur.fetchall()))
    komanda = """INSERT INTO progeKraji(proga, postaja, zaporedna_st, razdalja) values"""
    for i in range(len(prIds)):
        prId = int(prIds[i])
        proga = prStr[i].split(",")
        razdalja = prRaz[i].split(",")
        for j, p in enumerate(proga):
            cur.execute(""" SELECT id FROM postaja
                            WHERE ime = '{}' """.format(p))
            posIds = cur.fetchall()
            posId = posIds[0][0]
            niz = "({}, {}, {}, {}),".format(prId, posId, j, int(razdalja[j]))
            komanda += niz
    cur.execute(komanda[:-1])
    

#------VOZNI RED----------------------------
def napolniTabeloVozniRed(cur):
    cur.execute(""" SELECT emso from zaposlen where naziv = 'strojevodja'""")
    vozEmss = cur.fetchall()

    cur.execute(""" SELECT id from vlak""")
    vlakIds = cur.fetchall()

    cur.execute(""" SELECT proga from progekraji
                    GROUP BY proga""")
    progaIds= np.transpose(cur.fetchall())[0]

    postajes = []
    casis1 = []
    casis2 = []
    vozniks = []
    vlaks = []
    progas = []
    voznjas = []

    vv = 0
    voz = vozEmss[0][0]
    vla = vlakIds[0][0]
    for id in progaIds:
        cur.execute(""" SELECT postaja from progekraji
                        WHERE proga = {}""".format(id))
        postaje = list(np.transpose(np.array(cur.fetchall()))[0])
        casiMedPostajami = [random.randint(5,15) for i in range(len(postaje)-1)]
        casiMedPostajami = [0] + casiMedPostajami
        t = 0
        j = 0
        vz = 0
        while(t<60*20 or j%len(postaje) != 0):
            p = postaje[j%len(postaje)]
            if p == postaje[0]:
                voz = vozEmss[vv%len(vozEmss)][0]
                vla = vlakIds[vv%len(vlakIds)][0]
                vv += 1
                t += 30
                vz += 1
                
            
            postajes.append(int(p))
            t = t + casiMedPostajami[j%len(postaje)]
            uraPrihod = cas.Cas.minVCas(t)
            casis1.append(uraPrihod)
            pavzaMin = random.randint(0,20)
            t += pavzaMin
            uraOdhod = cas.Cas.minVCas(t)
            if (j+1)%len(postaje) == 0:
                uraOdhod = uraPrihod
            casis2.append(uraOdhod)
            voznjas.append(vz)           
            vozniks.append(voz)
            vlaks.append(vla)
            progas.append(id)


            j += 1
        


    llist = np.array([postajes, casis1, casis2, vozniks, vlaks, progas, voznjas])
    vnosVozniRed = transponiraj2(llist)
    
    komanda = """INSERT INTO voznired(postaja, cas_prihoda, cas_odhoda, voznik, vlak, proga, voznja) values"""
    for val in vnosVozniRed:
        idp = val[0]
        cp = val[1]
        co = val[2]
        vo = val[3]
        vl = val[4]
        pr = val[5]
        vz = val[6]
        niz = "({}, '{}', '{}', {}, '{}', {}, {}),".format(idp, cp, co, vo, vl, pr, vz)
        komanda += niz
    cur.execute(komanda[:-1])
    

    
def izbrisiCeloTabelo(cur, tabela):
    komanda = """ DELETE FROM {}
    """.format(tabela)

    cur.execute(komanda)

def datum(d):
    return "'{}-{}-{}'".format(d[2], d[1], d[0])
