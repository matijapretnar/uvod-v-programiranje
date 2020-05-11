from datetime import date
from model import Proracun, Racun, Kuverta, Preliv

moj_proracun = Proracun()

gotovina = moj_proracun.dodaj_racun('gotovina')
tekoci_racun = moj_proracun.dodaj_racun('tekoči račun')

vreca = moj_proracun.dodaj_kuverto('💰')

Preliv(230, date(2020, 4, 1), 'štipendija', tekoci_racun, vreca)
Preliv(-30, date(2020, 4, 3), 'prevoz', tekoci_racun, vreca)
Preliv(-40, date(2020, 4, 5), 'hlače', gotovina, vreca)
Preliv(150, date(2020, 4, 20), 'krizni dodatek', tekoci_racun, vreca)
Preliv(-150, date(2020, 4, 20), 'hlače', tekoci_racun, vreca)
Preliv(-100, date(2020, 4, 30), 'najemnina', tekoci_racun, vreca)
Preliv(-10, date(2020, 4, 30), 'telefon', tekoci_racun, vreca)
Preliv(-40, date(2020, 5, 4), 'hrana', gotovina, vreca)

print(moj_proracun)
