import auth
from baze import *
from simulacijaPodatkov import *
import psycopg2, psycopg2.extensions, psycopg2.extras

psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)

import csv

conn = psycopg2.connect(dbname = auth.db, host = auth.host, user = auth.user, password = auth.password)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

def ustvariTabeloModel():
    komanda = """
        CREATE TABLE model(
            id SERIAL PRIMARY KEY,
            kapaciteta INTEGER NOT NULL,
            teza FLOAT,
            ime TEXT
        )
    """
    cur.execute(komanda)
    conn.commit()

def ustvariTabeloVlak():
    komanda = """
        CREATE TABLE vlak(
            id SERIAL PRIMARY KEY,
            leto_izdelave INTEGER NOT NULL,
            model INTEGER REFERENCES model(id)
        )
    """
    cur.execute(komanda)
    conn.commit()

def ustvariTabeloZaposlen():
    komanda = """
        CREATE TABLE zaposlen(
            emso TEXT PRIMARY KEY,
            ime TEXT NOT NULL,
            rojstvo DATE NOT NULL,
            naslov TEXT NOT NULL,
            datum_zaposlitve  DATE NOT NULL,
            naziv TEXT NOT NULL
        )
    """
    cur.execute(komanda)
    conn.commit()

def ustvariTabeloPregled():
    komanda = """
        CREATE TABLE pregled(
            id SERIAL PRIMARY KEY,
            komentar TEXT NOT NULL,
            zaposleni TEXT REFERENCES zaposlen(emso),
            datum_pregleda DATE NOT NULL,
            vlak INTEGER NOT NULL REFERENCES vlak(id)
        )
    """
    cur.execute(komanda)
    conn.commit()

def ustvariTabeloVozovnica():
    komanda = """
    CREATE TABLE vozovnica(
        ime TEXT PRIMARY KEY,
        cas_veljavnost INT NOT NULL,
        cena FLOAT NOT NULL,
        opis TEXT
        )
    """
    cur.execute(komanda)
    conn.commit()

def ustvariTabeloPotnik():
    komanda = """
    CREATE TABLE potnik(
        emso TEXT PRIMARY KEY,
        ime TEXT NOT NULL,
        rojstvo DATE NOT NULL,
        naslov TEXT NOT NULL,
        mail TEXT NOT NULL UNIQUE,
        geslo TEXT NOT NULL,
        vozovnica INTEGER REFERENCES vozovnica(id),
        datum_veljavnosti DATE 

        )
    """
    cur.execute(komanda)
    conn.commit()

def ustvariTabeloUporabnik():
    komanda = """
    CREATE TABLE uporabnik(
        emso TEXT PRIMARY KEY,
        ime TEXT NOT NULL,
        rojstvo DATE NOT NULL,
        naslov TEXT NOT NULL,
        vozovnica INTEGER REFERENCES vozovnica(id),
        datum_veljavnosti DATE,
        mail TEXT NOT NULL UNIQUE,
        geslo TEXT NOT NULL
        )
    """
    cur.execute(komanda)
    conn.commit()

def ustvariTabeloVozovnica():
    komanda = """
    CREATE TABLE vozovnica(
        id INTEGER PRIMARY KEY, 
        ime TEXT NOT NULL,
        cena FLOAT NOT NULL,
        velja INT NOT NULL,
        opis TEXT)
    """
    cur.execute(komanda)
    conn.commit()

def ustvariTabeloPostaja():
    komanda = """
    CREATE TABLE postaja(
        id SERIAL PRIMARY KEY, 
        ime TEXT NOT NULL
        )
    """
    cur.execute(komanda)
    conn.commit()

def ustvariTabeloVoznja():
    komanda = """
    CREATE TABLE voznja(
        potnik TEXT REFERENCES potnik(emso), 
        datum DATE NOT NULL,
        ura TIME NOT NULL,
        vstopna_postaja INTEGER REFERENCES postaja(id),
        iztopna_postaja INTEGER REFERENCES postaja(id),
        PRIMARY KEY (potnik, datum, ura)
        )
    """
    cur.execute(komanda)
    conn.commit()

def ustvariTabeloProga():
    komanda = """
    CREATE TABLE proga(
        id INTEGER PRIMARY KEY,
        seznam_postaj TEXT NOT NULL
        )
    """
    cur.execute(komanda)
    conn.commit()

def ustvariTabeloVozniRed():
    komanda = """
    CREATE TABLE vozniRed(
        postaja INTEGER REFERENCES postaja(id),
        cas_prihoda TIME NOT NULL,
        cas_odhoda TIME NOT NULL,
        voznik TEXT REFERENCES zaposlen(emso),
        vlak INTEGER REFERENCES vlak(id),
        proga INTEGER REFERENCES proga(id),
        voznja INTEGER NOT NULL,
        PRIMARY KEY(proga, voznja, postaja)
        )
    """
    cur.execute(komanda)
    conn.commit()

def ustvariTabeloProgeKraji():
    komanda = """ CREATE TABLE progeKraji(
                proga INTEGER,
                postaja INTEGER,
                zaporedna_st INTEGER,
                PRIMARY KEY(proga, postaja)
                )
    """
    cur.execute(komanda)
    conn.commit()

def zbrisiTabelo(cur, ImeTabele):
    komanda = """
        DROP TABLE {}
    """.format(ImeTabele)
    komanda += " CASCADE"
    cur.execute(komanda)

def izbrisiVse(cur, tabele):
    for tabela in tabele:
        zbrisiTabelo(cur, tabela)
