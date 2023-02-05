import re

# Quantificadores (Contam)
# * 0 ou n ou {0,}
# + 1 ou n ou {1,}
# ? 0 ou 1
# {n} ou {min, max}
# {10,} 10 ou mais
# {,10} De zero a 10
# {10} Especificamente 10
# {5,10} De 5 a 10
# ()+ [a-zA-Z0-9]+
texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970, Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente. 
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de 
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso 
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

regexp = re.compile(r"jo+ão+", flags=re.I)
print(regexp.findall(texto))
print(regexp.sub("Felipe", texto))
print(re.findall("[Vv]e{3}m{2}", texto, flags=re.I))
print(re.findall("j[a-zA-Z]+ã[a-zA-Z]+", texto, flags=re.I))
print(re.findall("j[o]+ã[o]+", texto, flags=re.I))

texto2 = "João ama ser amado"

print(re.findall("ama[a-zA-Z]*[a-zA-Z]*", texto2, flags=re.I))
print(re.findall("ama[od]*", texto2, flags=re.I))
print(re.findall("ama[od]{0,2}", texto2, flags=re.I))
