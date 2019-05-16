import bottle
import random

@bottle.get('/')
def pozdravi():
    pozdrav = '{}, kdorkoli že si!'.format(random.choice(['Dober dan', 'Živjo', 'Zdravo']))
    return pozdrav

@bottle.get('/vprasaj-kako-si/')
def vprasaj_kako_si():
    pozdrav = '{}, kako si?'.format(random.choice(['Dober dan', 'Živjo', 'Zdravo']))
    return pozdrav

@bottle.get('/vprasaj-kako-si/<ime>/')
def vprasaj_kako_si_po_imenu(ime):
    return bottle.template('pozdrav.tpl', ime=ime)


bottle.run(debug=True, reloader=True)