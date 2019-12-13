// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

    // Copy R0 & R1 to ram0 & ram1. Use ram2 to store the output value.
    @R0
    D = M
    @ram0
    M = D

    @R1
    D = M
    @ram1
    M = D

    @ram2
    M = 0

    // If either ram0 or ram1 is 0, jump to OUTPUT.
    @ram0
    D = M
    @OUTPUT
    D; JEQ

    @ram1
    D = M
    @OUTPUT
    D; JEQ

(LOOP)
    // Add ram0 to ram2, which is the result, repeatedly.
    @ram0
    D = M
    @ram2
    M = D + M
    // Decrease ram1 by 1 in each loop.
    @ram1
    M = M - 1

    // Exit the loop if ram1 has decreased to 0.
    @ram1
    D = M
    @OUTPUT
    D; JEQ

    @LOOP
    0; JMP

(OUTPUT)
    // Copy data from ram2 to R2.
    @ram2
    D = M
    @R2
    M = D

    @END
    0; JMP

(END)
    @END
    0; JMP
    
