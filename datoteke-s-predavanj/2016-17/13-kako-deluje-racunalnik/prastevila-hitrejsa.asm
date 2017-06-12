PUSH 2
MOV C, 3

preveri_ali_je_C_prastevilo:
; v D bomo shranjevali možne delitelje
; prvi možni je 3
MOV D, 3

  preveri_ali_D_deli_C:
    ; če je D večji od C, je C praštevilo
    MOV A, D
    MUL A
    CMP C, A
    JB C_je_prastevilo

    ; sicer pogledamo, če D deli C
    MOV A, C
    DIV D
    MUL D
    CMP A, C

    ; če D deli C, potem pojdi na naslednji C
    JE pojdi_na_naslednji_C

    ; če D ne deli C, povečaj D in ponovi vajo
    ADD D, 2
    JMP preveri_ali_D_deli_C

  C_je_prastevilo:
    PUSH C

pojdi_na_naslednji_C:
ADD C, 2
JMP preveri_ali_je_C_prastevilo