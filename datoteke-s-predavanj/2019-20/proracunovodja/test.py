import json
from datetime import date
from model import Proracun

proracun = Proracun()

gotovina = proracun.nov_racun('gotovina')
tekoci_racun = proracun.nov_racun('tekoči račun')
vreca = proracun.nov_kuverto('💰')

proracun.nov_preliv(230, date(2020, 4, 1), 'štipendija', tekoci_racun, vreca)
proracun.nov_preliv(-30, date(2020, 4, 3), 'prevoz', tekoci_racun, vreca)
proracun.nov_preliv(-40, date(2020, 4, 5), 'hlače', gotovina, vreca)
proracun.nov_preliv(150, date(2020, 4, 20), 'krizni dodatek', tekoci_racun, vreca)
proracun.nov_preliv(-150, date(2020, 4, 20), 'hlače', tekoci_racun, vreca)
proracun.nov_preliv(-100, date(2020, 4, 30), 'najemnina', tekoci_racun, vreca)
proracun.nov_preliv(-10, date(2020, 4, 30), 'telefon', tekoci_racun, vreca)
proracun.nov_preliv(-40, date(2020, 5, 4), 'hrana', gotovina, vreca)

stanje = proracun.v_slovar()
with open('stanje.json', 'w') as datoteka:
    json.dump(stanje, datoteka, ensure_ascii=False, indent=4)
