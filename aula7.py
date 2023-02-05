import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970, Maria era o nome dela.

Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente. 
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de 
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso 
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

# re.A re.ASCII => Uma flag para não pegar as letras acentuadas

# \w+ = [a-zA-Z0-9À-ú_]+
# \w+ + flags=re.A = [a-zA-Z0-9_]+
# \W+ = [^a-zA-Z0-9À-ú_]+ # Seria o inverso do \w+
# \d = [0-9] # Pega apenas os números
# \D = [^0-9]
# \s = [ \r\n\v\f\t] # Pega todos os espaços
# \S = [^ \r\n\v\f\t] # Pega todos os caracteres sem ser espaço
# \b = \bflo\w+ # Localiza todas as palavras que contém o inicial "flo", com qualquer letra após (\w+).
# Portanto, a borda pode ser inicial ou final
# \B = Se o caractere digitado estiver uma borda, não conta

# re.M = Multiline => ^ $
# re.S -> Dotall
print(re.findall(r'[^,.:! \n_"]+', texto, flags=re.I))
# À-ú Pega todas as letras acentuadas
print(re.findall(r"[a-zA-Z0-9À-ú]+", texto))
# Um atalho que vai ter  o mesmo resultado dado acima, # além disso,
# obtenha-se outras formatações de idioma que contém acentos e etc.
print(re.findall(r"\w+", texto, flags=re.A))
print(re.findall(r"[À-ú]", texto))
print(re.findall(r"\d+", texto))
print(re.findall(r"\S+", texto))
print(re.findall(r"\be\w+", texto, flags=re.I))
print(re.findall(r"\w+e\b", texto, flags=re.I))
print(re.findall(r"\b[a-zA-ZÀ-ú]{4}\b", texto, flags=re.I))
print(re.findall(r"flores\B", texto, flags=re.I))
