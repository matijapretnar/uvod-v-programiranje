print('Dober dan, jaz sem super kalkulator.')
while True:
    try:
        racun = input('Kaj bi rad izračunal? ')
        print('Za izračun nujno potrebujem veliko energije.')
        print('Jedrski reaktor dajem na maksimum.')
        prvi, op, drugi = racun.split()
        x, y = int(prvi), int(drugi)
        if op == '+':
            rezultat = x + y
        elif op == '*':
            rezultat = x * y
        elif op == '-':
            rezultat = x - y
        elif op == '/':
            rezultat = x / y
        else:
            raise Exception('Ta operator ne obstaja')
        print('Ugotovil sem, da je {} = {}'.format(racun, rezultat))
    except ZeroDivisionError:
        print('Delil si z nič. Kaj ne veš, da se to ne sme?')
    except ValueError:
        print('Vnos ni oblike ŠTEVILO OPERACIJA ŠTEVILO, na primer 3 + 10')
    finally:
        print('Izklapljam jedrski reaktor.')



