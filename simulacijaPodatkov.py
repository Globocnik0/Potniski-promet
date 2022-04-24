import random
import exrex as ex
import numpy as np

def transponiraj(a1, a2):
    vnos = np.array([a1, a2])
    vnos = np.transpose(vnos)
    return vnos


#----MODEL---------
capList = [50, 100, 150, 200, 300]
tezaList = [10, 12, 20, 20, 23]
vnosModel = transponiraj(capList, tezaList)


def napolniTabeloModel(vnos):
    komanda = """INSERT INTO model(kapaciteta, teza) values"""
    for val in vnos:
        niz = "({}, {}),".format(val[0], val[1])
        komanda += niz
    return komanda[:-1] #znebimo se zadnje vejice

#----VLAK----------------
def napolniTabeloVlak(con, cur, stVnosov):
    cur.execute(""" SELECT id from model""")
    modeliNaVoljo = cur.fetchall()
    letaIzdelava = [random.randint(1980, 2020) for m in range(stVnosov)]
    modeli = [modeliNaVoljo[random.randint(0, len(modeliNaVoljo)-1)][0] for m in range(stVnosov)]
    vnosVlak = transponiraj(letaIzdelava, modeli)

    komanda = """INSERT INTO vlak(leto_izdelave, model) values"""
    for val in vnosVlak:
        niz = "({}, {}),".format(val[0], val[1])
        komanda += niz
    return komanda[:-1]




def izbrisiCeloTabelo(tabela):
    komanda = """ DELETE FROM {}
    """.format(tabela)

    return komanda


