def kvadrati_ki_pri_deljenju_s_7_dajo_ostanek_2_z_zanko(n):
    kvadrati = []
    for i in range(n):
        i2 = i ** 2
        if i2 % 7 == 2:
            kvadrati.append(i2)
    return kvadrati

def kvadrati_ki_pri_deljenju_s_7_dajo_ostanek_2_z_izpeljanim_seznamom(n):
    return [i ** 2 for i in range(n) if i ** 2 % 7 == 2]

def kvadrati_ki_pri_deljenju_s_7_dajo_ostanek_2_z_mrozem(n):
    return [i2 for i in range(n) if (i2 := i ** 2) % 7 == 2]
