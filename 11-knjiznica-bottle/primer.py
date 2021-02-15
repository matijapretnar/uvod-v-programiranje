import bottle

@bottle.get('/<ime>/')
def pozdravi(ime):
    return bottle.template('zivjo.tpl', ime=ime)

@bottle.get('/sestej/')
def sestej():
    a = bottle.request.query['a']
    b = bottle.request.query['b']
    return '{} + {} = {}'.format(a, b, a + b)

bottle.run(debug=True, reloader=True)