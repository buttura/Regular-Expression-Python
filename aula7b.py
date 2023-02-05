# re.A -> ASCII
# re.I -> IGNORECASE
# re.M -> MULTILINE = ^ $ = Começo e fim de linha
# re.S -> DOTALL = Reconhece as quebras de linhas, assim não considerando apenas a linha

import re

texto = """
131.768.460-53
055.123.060-50
955.123.060-90
"""
print(re.findall(r"((?:\d{3}\.){2}\d{3}-\d{2})", texto, re.M | re.S))

texto2 = "O João gosta de folia \n E adora ser amado"
