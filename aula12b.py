import re

SenhasFortes = """
TODOS OS CARACTERES
$pgWE7'2Y+8e
6Ow0zW+7#v,P
2UbO%!$rcH53
m7l,V/6)OUe2
l(21Cg8i$PL"

SEM MINÚSCULAS
5O),7"D5(6CN
4Z&,2IE!46J%
YJ&10'5&PW2)
9"4N&A,BI34&
&0#G*4!9IY8Z

SEM MINÚSCULAS E NÚMEROS
*HQX%,WV(*H"
SR-R&/XI"+-C
)F'N*C#,SXI(
R)RI%Z%S#P&%
.L.LX$#KN,+Z
"""

#SenhaRegEx = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[\u0020-\u002F]).{12,}$", flags=re.M)
SenhaRegEx = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[.\-*_%^&()!@#$]).{12}$", flags=re.M)
print(SenhaRegEx.findall(SenhasFortes))