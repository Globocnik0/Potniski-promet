

def je_prestopno(leto):
    if leto % 400 == 0:
        return True
    elif leto % 100 == 0:
        return False
    elif leto% 4 == 0:
        return True
    else:
        return False

def stevilo_dni(leto):
    return (366 if je_prestopno(leto) else 365)

def dolzine_mesecev(leto):
    return [
        31, (29 if je_prestopno(leto) else 28), 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    ]

class Datum:

    def __init__(self, dan, mesec, leto):
        self.dan = dan
        self.mesec = mesec
        self.leto = leto

    def __str__(self):
        return f"{self.dan}. {self.mesec}. {self.leto}"


    def __repr__(self):
        return f"Datum({self.dan}, {self.mesec}, {self.leto})"

    def je_veljaven(self):
        if self.mesec > 12:
            return False
        meseci = dolzine_mesecev(self.leto)
        if self.dan > meseci[self.mesec-1]:
            return False
        else:
            return True

    def __lt__(self, other):
        return ((self.leto, self.mesec, self.dan) < (other.leto, other.mesec, other.dan))

    def __eq__(self, other):
        return ((self.leto, self.mesec, self.dan)==(other.leto, other.mesec, other.dan))

    def dan_v_letu(self):
        meseci = dolzine_mesecev(self.leto)
        dnevi = self.dan
        vsota = sum(meseci[0:self.mesec-1]) + dnevi
        return vsota

    def dni_od_zacetka(self):
        st_prestopnih = (self.leto-1)//4
        st_pre_nepre = (self.leto-1)//100
        st_pre_ne_pre = (self.leto-1)//2000
        dnevi = (self.leto-1)*365 + st_prestopnih - st_pre_nepre + st_pre_ne_pre + self.dan_v_letu()
        return dnevi
    
    def razlika(self, other):
        return (self.dni_od_zacetka() - other.dni_od_zacetka())
    
    
    """def razlika(self, other):
        
        def dan_v_letu(datum):
            meseci = dolzine_mesecev(datum.leto)
            dnevi = datum.dan
            vsota = sum(meseci[0:datum.mesec-1]) + dnevi
            return vsota

        def dni_od_zacetka(datum):
            st_prestopnih = (datum.leto-1)//4
            st_pre_nepre = (datum.leto-1)//100
            st_pre_ne_pre = (datum.leto-1)//2000
            dnevi = (datum.leto-1)*365 + st_prestopnih - st_pre_nepre + st_pre_ne_pre + dan_v_letu(datum)
            return dnevi
        
        return dni_od_zacetka(self) - dni_od_zacetka(other)"""
    

    def dan_v_tednu(self):
        pon = Datum(7,12,2020)
        return self.razlika(pon)%7 + 1

    @staticmethod
    def dan_v_letu_stat(leto, dan):
        meseci = dolzine_mesecev(leto)
        for i in range(13):
            if sum(meseci[:i]) >= dan:
                mesec = i
                break
        dan = dan - sum(meseci[:i-1])
        return Datum(dan, mesec, leto)


class Cas:

    def __init__(self, ura, minuta, sekunda):
        self.ura = ura
        self.min = minuta
        self.sec = sekunda

    def __str__(self):
        return f"{self.ura}:{self.min}:{self.sec}"


    def preveriCas(this):
        while(True):
            if this.sec > 59:
                this.sec -= 60
                this.min +=1
            elif this.min > 59:
                this.min -= 60
                this.ura += 1
            elif this.ura > 23:
                this.ura -= 24
            elif this.ura < 24:
                break
        

    def casPlusSec(this, sek):
        h = sek // 3600
        sek = sek - h*3600
        m = sek//60
        sek = sek - m*60
        s = sek
        return Cas(h, m, s)

    def casPlusMin(this, minn):
        vseMinute = this.ura*60 + this.min + minn
        h = vseMinute // 60
        minn = vseMinute % 60
        return Cas(h, minn, 0)    

    def secVCas(sek):
        h = sek // 3600
        sek = sek - h*3600
        m = sek//60
        sek = sek - m*60
        s = sek

        return Cas(h, m, s)

    def minVCas(min):
        h = min // 60
        m = min - h*60

        return Cas(h, m, 0)

