# ocenimo število učiteljev matematike v osnovnih šolah

stevilo_slovencev = 2000000  # človek
pricakovana_zivljenska_doba = 120  # leto
velikost_generacije = stevilo_slovencev / pricakovana_zivljenska_doba  # človek / leto
stevilo_osnovnosolcev = 9 * velikost_generacije  # človek
stevilo_razredov = stevilo_osnovnosolcev / 24  # razred
stevilo_ur_matematike_na_teden = stevilo_razredov * 4  # ura matematike / teden
stevilo_uciteljev_matematike = stevilo_ur_matematike_na_teden / 20  # človek

# ocenimo število učiteljev matematike v osnovnih šolah

s=2000000
p=120
v=s/p
o=9*v
r=o/24
m=r*4
u=m/20
