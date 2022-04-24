

def ustvariTabeloModel():
    komanda = """
        CREATE TABLE model(
            id SERIAL PRIMARY KEY,
            kapaciteta INTEGER NOT NULL,
            teza FLOAT
        )
    """
    return komanda

def ustvariTabeloVlak():
    komanda = """
        CREATE TABLE vlak(
            id SERIAL PRIMARY KEY,
            leto_izdelave INTEGER NOT NULL,
            model INTEGER REFERENCES model(id)
        )
    """
    return komanda

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
    return komanda

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
    return komanda

def ustvariTabeloVozovnica():
    komanda = """
    CREATE TABLE vozovnica(
        ime TEXT PRIMARY KEY,
        cas_veljavnost INT NOT NULL,
        cena FLOAT NOT NULL,
        opis TEXT
        )
    """
    return komanda


def ustvariTabeloPotnik():
    komanda = """
    CREATE TABLE potnik(
        emso TEXT PRIMARY KEY,
        ime TEXT NOT NULL,
        vozovnica TEXT REFERENCES vozovnica(ime),
        datum_veljavnosti DATE NOT NULL
        )
    """
    return komanda

def ustvariTabeloPostaja():
    komanda = """
    CREATE TABLE postaja(
        id INTEGER PRIMARY KEY, 
        datum DATE NOT NULL,
        ura TIME NOT NULL
        )
    """
    return komanda

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
    return komanda

def ustvariTabeloProga():
    komanda = """
    CREATE TABLE proga(
        id INTEGER PRIMARY KEY,
        seznam_postaj TEXT NOT NULL
        )
    """
    return komanda

def ustvariTabeloVozniRed():
    komanda = """
    CREATE TABLE vozniRed(
        postaja INTEGER REFERENCES postaja(id),
        cas_prihoda TIME NOT NULL,
        cas_odhoda TIME NOT NULL,
        zamuda TIME,
        voznik TEXT REFERENCES zaposlen(emso),
        vlak INTEGER REFERENCES vlak(id),
        proga INTEGER REFERENCES proga(id),
        PRIMARY KEY(vlak, cas_prihoda, postaja)
        )
    """
    return komanda


def zbrisiTabelo(ImeTabele):
    komanda = """
        DROP TABLE {}
    """.format(ImeTabele)
    return komanda