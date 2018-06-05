JMP main

; Kvadrira vrednost v A
kvadriraj:
    MUL A
    RET

; Nastavi C = A^2 + B^2
f:
    PUSH A
    PUSH B
    CALL kvadriraj
    MOV C, A
    MOV A, B
    CALL kvadriraj
    ADD C, A
    POP B
    POP A
    RET


main:
    MOV A, 3
    MOV B, 4
    CALL f
