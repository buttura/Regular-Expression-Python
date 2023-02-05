# Meta caracteres:
# ^ -> Começa com
# $ -> Termina com
# [^a-z] -> Negação | Pegue qualquer letra SEM QUE SEJA entre a e z
import re

cpf = "147.852.963-12"
print(re.findall(r"^((?:[0-9]{3}.){2}[0-9]{3}-[0-9]{2})$", cpf))
