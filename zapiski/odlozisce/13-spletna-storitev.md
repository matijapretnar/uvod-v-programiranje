# Spletna storitev

## Piškotki

Podatke si lahko shranjujemo v **piškotke** na uporabnikovem računalniku

```
@bottle.post('/glasuj/')
def glasuj():
  piskot = bottle.request.get_cookie('glas')
  if piskot is None:
    glas = bottle.request.forms['glas']
    model.zabelezi_glas(glas)
    bottle.response.set_cookie('glas', glas)
    bottle.redirect('/glasuj/')
  else:
    return 'Ne glasuj dvakrat!'
```

## Uporaba gesel

knjižnica `hashlib`
