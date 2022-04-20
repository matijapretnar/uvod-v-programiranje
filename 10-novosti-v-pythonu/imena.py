def predstavi_se(ime):
    imena = ime.split()
    if len(imena) == 1:
        print(f"Sem {imena[0]}")
    elif len(imena) == 2:
        ime, priimek = imena
        print(f"{priimek}, {ime} {priimek}")
    else:
        ime, *vmesna, priimek = imena
        print(f"{ime} {'. '.join(vmesno[0] for vmesno in vmesna)}. {priimek}")

def predstavi_se(ime):
    match ime.split():
        case [("Janez" | "Jani") as ime]:
            print(f"Sem {ime}, ampak prijatelji me kličejo Đoni")
        case [ime] if len(ime) > 10:
            print(f"Sem {ime}, na kratko pa kar {ime[:5]}")
        case [ime]:
            print(f"Sem {ime}")
        case [ime, priimek]:
            print(f"{priimek}, {ime} {priimek}")
        case [ime, *vmesna, priimek]:
            print(f"{ime} {'. '.join(vmesno[0] for vmesno in vmesna)}. {priimek}")
