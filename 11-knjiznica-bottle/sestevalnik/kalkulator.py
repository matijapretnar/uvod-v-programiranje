import bottle

@bottle.get('/')
def osnovna_stran():
    return bottle.template('sestej.tpl')

@bottle.post('/sestej/')
def sestej():
    a = int(bottle.request.forms['a'])
    b = int(bottle.request.forms['b'])
    return '{} + {} = {}'.format(a, b, a + b)

@bottle.get('/pozdravi/')
def pozdravi():
  ime = bottle.request.query.getunicode('ime')
  return 'Živjo, {}!'.format(ime)

bottle.run(debug=True, reloader=True)