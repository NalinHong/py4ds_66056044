from src.ex07 import *


def test_print_ascii_table(capsys):
    print_ASCII_table(32, 126)  # ตรงนี้ให้ใช้ตัวเลข 32-126 ไปได้เลย
    captured = capsys.readouterr()
    assert captured.out == """ 
!
"
#
$
%
&
'
(
)
*
+
,
-
.
/
0
1
2
3
4
5
6
7
8
9
:
;
<
=
>
?
@
A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
[
\\
]
^
_
`
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z
{
|
}
~
"""