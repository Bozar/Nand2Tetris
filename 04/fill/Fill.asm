// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

    // Set colors: black & white.
    @32767
    D = A
    D = D + 1
    D = D + A
    @black
    M = D

    @0
    D = A
    @white
    M = D

    // Note that KBD is adjacent to the last SCREEN RAM.
    @KBD
    D = A
    @last
    M = D

    // The current SCREEN RAM address.
    @current

(INPUT)
    // Reset `current`.
    @SCREEN
    D = A
    @current
    M = D

    // Print a black or white screen based on input.
    @KBD
    D = M
    @WHITESCREEN
    D; JEQ
    @BLACKSCREEN
    0; JMP

(BLACKSCREEN)
    // if (@current == @last), the full screen has been drawn.
    @current
    D = M
    @last
    D = M - D
    @INPUT
    D; JEQ

    // Load color: black.
    @black
    D = M
    // Set RAM address.
    @current
    A = M
    // Set RAM content.
    M = D

    // Update @current.
    A = A + 1
    D = A
    @current
    M = D

    @BLACKSCREEN
    0; JMP

(WHITESCREEN)
    @current
    D = M
    @last
    D = M - D
    @INPUT
    D; JEQ

    // Load color: white.
    @white
    D = M
    @current
    A = M
    M = D

    A = A + 1
    D = A
    @current
    M = D

    @WHITESCREEN
    0; JMP

