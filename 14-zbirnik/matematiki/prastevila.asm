PUSH 2

MOV C, 3

ali_je_C_prastevilo:
MOV D, 3

ali_D_deli_C:
CMP C, D
JE je_prastevilo

MOV A, C
DIV D
MUL D
CMP A, C
JE ni_prastevilo
ADD D, 2
JMP ali_D_deli_C

ni_prastevilo:
ADD C, 2
JMP ali_je_C_prastevilo

je_prastevilo:
PUSH C
ADD C, 2
JMP ali_je_C_prastevilo
