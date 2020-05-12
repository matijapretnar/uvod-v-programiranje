from datetime import date
from model import Proracun

proracun = Proracun()

gotovina = proracun.dodaj_racun('gotovina')
tekoci_racun = proracun.dodaj_racun('tekoči račun')
vreca = proracun.dodaj_kuverto('💰')

proracun.dodaj_preliv(230, date(2020, 4, 1), 'štipendija', tekoci_racun, vreca)
proracun.dodaj_preliv(-30, date(2020, 4, 3), 'prevoz', tekoci_racun, vreca)
proracun.dodaj_preliv(-40, date(2020, 4, 5), 'hlače', gotovina, vreca)
proracun.dodaj_preliv(150, date(2020, 4, 20), 'krizni dodatek', tekoci_racun, vreca)
proracun.dodaj_preliv(-150, date(2020, 4, 20), 'hlače', tekoci_racun, vreca)
proracun.dodaj_preliv(-100, date(2020, 4, 30), 'najemnina', tekoci_racun, vreca)
proracun.dodaj_preliv(-10, date(2020, 4, 30), 'telefon', tekoci_racun, vreca)
proracun.dodaj_preliv(-40, date(2020, 5, 4), 'hrana', gotovina, vreca)

print(proracun)
