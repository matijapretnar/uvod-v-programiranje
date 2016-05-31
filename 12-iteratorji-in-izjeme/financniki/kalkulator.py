print('Pozdravljen v fantastičnem kalkulatorju!')
while True:
    try:
        racun = input('Kaj bi rad izračunal? ')
        print('Odpiram plin na pečici.')
        x, op, y = racun.split()
        if op == '+':
            rezultat = int(x) + int(y)
        elif op == '*':
            rezultat = int(x) * int(y)
        elif op == '-':
            rezultat = int(x) - int(y)
        elif op == '/':
            rezultat = int(x) / int(y)
        else:
            rezultat = '?'
        print('Izračunal sem, da je {} = {}.'.format(racun, rezultat))
    except ZeroDivisionError:
        print('Na žalost sem delil z 0, zato ti ne morem dati odgovora.')
    except ValueError:
        print('Tvoj vnos je napačen. Bodi bolj natančen!')
    except KeyboardInterrupt:
        print('Vidim, da me ne maraš več. Na tej točki se posloviva.')
        break
    except:
        print('Spet si nekaj polomil!')
    finally:
        print('Zapiram plin na pečici.')

