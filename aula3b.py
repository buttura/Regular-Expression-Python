import re
# + 1 ou n
# * 0 ou n
# ? 0 ou 1
# {max, min}
# {numero espicifico}
# [a-zA-Z0-9]+

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
print(re.findall(r"jo{1,}ão{1,}", texto, flags=re.I))
print(re.findall(r"j[a-zA-Z0-9]+ã[a-zA-Z0-9]+", texto, flags=re.I))

texto2 = "João ama de ser amado"

print(re.findall(r"ama[od]*", texto2, flags=re.I))
print(re.findall(r"ama[od]{0,2}", texto2, flags=re.I))
