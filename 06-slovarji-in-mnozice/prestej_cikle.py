def v_seznamu_seznamov_se_vsak_element_pojavi_najvec_trikrat(cikli):
    ze_videni = set()
    for cikel in cikli:
        for element in cikel:
            if element <= 0:
                return False
            elif element in ze_videni:
                return False
            else:
                ze_videni.add(element)
    return True


def v_seznamu_seznamov_se_vsak_element_pojavi_najvec_trikrat(cikli):
    st_pojavitev = {}
    for cikel in cikli:
        for element in cikel:
            if element <= 0:
                return False
            pojavitve_elementa = st_pojavitev.get(element, 0)
            if pojavitve_elementa > 3:
                return False
            else:
                st_pojavitev[element] = pojavitve_elementa + 1
    return True
