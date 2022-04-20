E ::=
    | True
    | False
    | E1 + E2
    | E1 * E2
    | E1 < E2
    | f(E1, ..., En)
    | [E1, ..., En]
    | {E1: E1', ..., En: En'}
    | E1 if E else E2
    | x := E
    | [E1 for x in E2]
    | lambda x: E

S ::=
    | E
    | if E:
          S1
      else:
          S2
    | x = E
    | return E
    | for x in E:
          S
    | S1
      S2
    | def f(x1, ..., xn):
        S
    | match E:
          case P1:
              S1
          case P2:
              S2

P ::=
    | x
    | True
    | False
    | [P1, ..., Pn]
    | P as x
    | (P1 | ... | Pn)
    | P if E
    | _