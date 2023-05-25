\Problem name: ULS

Minimize
OBJROW: 3000 Y0 + 3000 Y1 + 3000 Y2 + 3000 Y3 + 3000 Y4 + 3000 Y5 + 3000 Y6 + 3000 Y7 + 3000 Y8 + 3000 Y9
 + 3000 Y10 + 3000 Y11 + 3000 Y12 + 3000 Y13 + 3000 Y14 + 3000 Y15 + 3000 Y16 + 3000 Y17 + 3000 Y18 + 3000 Y19
 + 3000 Y20 + 5 X0 + 3 X1 + 4 X2 + 5 X3 + 6 X4 + 3 X5 + 4 X6 + 5 X7 + 3 X8
 + 4 X9 + 5 X10 + 6 X11 + 3 X12 + 4 X13 + 5 X14 + 3 X15 + 4 X16 + 5 X17 + 6 X18
 + 3 X19 + 4 X20 + 2 S0 + 2 S1 + 2 S2 + 2 S3 + 2 S4 + 2 S5 + 2 S6 + 2 S7
 + 2 S8 + 2 S9 + 2 S10 + 2 S11 + 2 S12 + 2 S13 + 2 S14 + 2 S15 + 2 S16 + 2 S17
 + 2 S18 + 2 S19 + 2 S20
Subject To
constr(0):  X0 - S0 = 30
constr(1):  - X0 + S0 = -30
constr(2):  X1 + S0 - S1 = 25
constr(3):  - X1 - S0 + S1 = -25
constr(4):  X2 + S1 - S2 = 15
constr(5):  - X2 - S1 + S2 = -15
constr(6):  X3 + S2 - S3 = 47
constr(7):  - X3 - S2 + S3 = -47
constr(8):  X4 + S3 - S4 = 34
constr(9):  - X4 - S3 + S4 = -34
constr(10):  X5 + S4 - S5 = 10
constr(11):  - X5 - S4 + S5 = -10
constr(12):  X6 + S5 - S6 = 15
constr(13):  - X6 - S5 + S6 = -15
constr(14):  X7 + S6 - S7 = 30
constr(15):  - X7 - S6 + S7 = -30
constr(16):  X8 + S7 - S8 = 25
constr(17):  - X8 - S7 + S8 = -25
constr(18):  X9 + S8 - S9 = 15
constr(19):  - X9 - S8 + S9 = -15
constr(20):  X10 + S9 - S10 = 47
constr(21):  - X10 - S9 + S10 = -47
constr(22):  X11 + S10 - S11 = 34
constr(23):  - X11 - S10 + S11 = -34
constr(24):  X12 + S11 - S12 = 10
constr(25):  - X12 - S11 + S12 = -10
constr(26):  X13 + S12 - S13 = 15
constr(27):  - X13 - S12 + S13 = -15
constr(28):  X14 + S13 - S14 = 30
constr(29):  - X14 - S13 + S14 = -30
constr(30):  X15 + S14 - S15 = 25
constr(31):  - X15 - S14 + S15 = -25
constr(32):  X16 + S15 - S16 = 15
constr(33):  - X16 - S15 + S16 = -15
constr(34):  X17 + S16 - S17 = 47
constr(35):  - X17 - S16 + S17 = -47
constr(36):  X18 + S17 - S18 = 34
constr(37):  - X18 - S17 + S18 = -34
constr(38):  X19 + S18 - S19 = 10
constr(39):  - X19 - S18 + S19 = -10
constr(40):  X20 + S19 - S20 = 15
constr(41):  - X20 - S19 + S20 = -15
constr(42):  -100000 Y0 + X0 <= -0
constr(43):  -100000 Y1 + X1 <= -0
constr(44):  -100000 Y2 + X2 <= -0
constr(45):  -100000 Y3 + X3 <= -0
constr(46):  -100000 Y4 + X4 <= -0
constr(47):  -100000 Y5 + X5 <= -0
constr(48):  -100000 Y6 + X6 <= -0
constr(49):  -100000 Y7 + X7 <= -0
constr(50):  -100000 Y8 + X8 <= -0
constr(51):  -100000 Y9 + X9 <= -0
constr(52):  -100000 Y10 + X10 <= -0
constr(53):  -100000 Y11 + X11 <= -0
constr(54):  -100000 Y12 + X12 <= -0
constr(55):  -100000 Y13 + X13 <= -0
constr(56):  -100000 Y14 + X14 <= -0
constr(57):  -100000 Y15 + X15 <= -0
constr(58):  -100000 Y16 + X16 <= -0
constr(59):  -100000 Y17 + X17 <= -0
constr(60):  -100000 Y18 + X18 <= -0
constr(61):  -100000 Y19 + X19 <= -0
constr(62):  -100000 Y20 + X20 <= -0
Bounds
 0 <= Y0 <= 1
 0 <= Y1 <= 1
 0 <= Y2 <= 1
 0 <= Y3 <= 1
 0 <= Y4 <= 1
 0 <= Y5 <= 1
 0 <= Y6 <= 1
 0 <= Y7 <= 1
 0 <= Y8 <= 1
 0 <= Y9 <= 1
 0 <= Y10 <= 1
 0 <= Y11 <= 1
 0 <= Y12 <= 1
 0 <= Y13 <= 1
 0 <= Y14 <= 1
 0 <= Y15 <= 1
 0 <= Y16 <= 1
 0 <= Y17 <= 1
 0 <= Y18 <= 1
 0 <= Y19 <= 1
 0 <= Y20 <= 1
Integers
Y0 Y1 Y2 Y3 Y4 Y5 Y6 Y7 Y8 Y9 
Y10 Y11 Y12 Y13 Y14 Y15 Y16 Y17 Y18 Y19 
Y20 X0 X1 X2 X3 X4 X5 X6 X7 X8 
X9 X10 X11 X12 X13 X14 X15 X16 X17 X18 
X19 X20 S0 S1 S2 S3 S4 S5 S6 S7 
S8 S9 S10 S11 S12 S13 S14 S15 S16 S17 
S18 S19 S20 
End
