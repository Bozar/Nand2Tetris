@256
D=A
@SP
M=D
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=M-D
@ARITHMETIC_TRUE_0
D;JEQ
@0
D=A
@ARITHMETIC_END_0
0;JMP
(ARITHMETIC_TRUE_0)
@0
D=!A
(ARITHMETIC_END_0)
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=M-D
@ARITHMETIC_TRUE_1
D;JEQ
@0
D=A
@ARITHMETIC_END_1
0;JMP
(ARITHMETIC_TRUE_1)
@0
D=!A
(ARITHMETIC_END_1)
@SP
A=M
M=D
@SP
M=M+1
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=M-D
@ARITHMETIC_TRUE_2
D;JEQ
@0
D=A
@ARITHMETIC_END_2
0;JMP
(ARITHMETIC_TRUE_2)
@0
D=!A
(ARITHMETIC_END_2)
@SP
A=M
M=D
@SP
M=M+1
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=M-D
@ARITHMETIC_TRUE_3
D;JLT
@0
D=A
@ARITHMETIC_END_3
0;JMP
(ARITHMETIC_TRUE_3)
@0
D=!A
(ARITHMETIC_END_3)
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=M-D
@ARITHMETIC_TRUE_4
D;JLT
@0
D=A
@ARITHMETIC_END_4
0;JMP
(ARITHMETIC_TRUE_4)
@0
D=!A
(ARITHMETIC_END_4)
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=M-D
@ARITHMETIC_TRUE_5
D;JLT
@0
D=A
@ARITHMETIC_END_5
0;JMP
(ARITHMETIC_TRUE_5)
@0
D=!A
(ARITHMETIC_END_5)
@SP
A=M
M=D
@SP
M=M+1
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=M-D
@ARITHMETIC_TRUE_6
D;JGT
@0
D=A
@ARITHMETIC_END_6
0;JMP
(ARITHMETIC_TRUE_6)
@0
D=!A
(ARITHMETIC_END_6)
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=M-D
@ARITHMETIC_TRUE_7
D;JGT
@0
D=A
@ARITHMETIC_END_7
0;JMP
(ARITHMETIC_TRUE_7)
@0
D=!A
(ARITHMETIC_END_7)
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=M-D
@ARITHMETIC_TRUE_8
D;JGT
@0
D=A
@ARITHMETIC_END_8
0;JMP
(ARITHMETIC_TRUE_8)
@0
D=!A
(ARITHMETIC_END_8)
@SP
A=M
M=D
@SP
M=M+1
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=D+M
@SP
A=M
M=D
@SP
M=M+1
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=M-D
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
D=-D
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=D&M
@SP
A=M
M=D
@SP
M=M+1
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=D|M
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
D=!D
@SP
A=M
M=D
@SP
M=M+1
(END_LOOP)
@END_LOOP
0;JMP