stevilo_slovencev = 2000000
pricakovana_starost = 77
velikost_generacije = stevilo_slovencev / pricakovana_starost
stevilo_osnovnosolcev = 9 * velikost_generacije
velikost_razreda = 25
stevilo_razredov = stevilo_osnovnosolcev / velikost_razreda
stevilo_ur_matematike = 4.5 * stevilo_razredov
stevilo_uciteljev = stevilo_ur_matematike / 20
delez = stevilo_uciteljev / stevilo_slovencev

# Isto kodo bi lahko napisali tudi takole, vendar je precej manj pregledna,
# pa še napako skriva. Jo najdete?
s=2000000;p=77;g=s/p;o=9*g;r=25;s=o/r;m=4.5*s;u=m/20;d=u/s
