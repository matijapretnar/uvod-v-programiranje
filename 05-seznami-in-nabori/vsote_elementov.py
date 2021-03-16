def vsota_seznama(sez):
    vsota = 0
    for x in sez:
        vsota += x
    return vsota


def sled_matrike(mat):
    sled = 0
    for i in range(len(mat)):
        sled += mat[i][i]
    return sled


# Ne pišimo tako, ker je po nepotrebnem preveč počasno:
# def sled_matrike(mat):
#     sled = 0
#     for i in range(len(mat)):
#         for j in range(len(mat)):
#             if i == j:
#                 sled += mat[i][j]
#     return sled
