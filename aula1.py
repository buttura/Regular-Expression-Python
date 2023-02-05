import re


string = "Esse é um teste de expressões teste regulares."
# Vai retornar a primeira ocorrencia da expressão regular digitada, mostrando a posição
print(re.search(r"teste", string))

# Vai retornar uma lista com todas as ocorrencias da expressão regular digitada
print(re.findall(r"teste", string))

# Substitui uma determinada palavra de uma variavel (string) a partir da expressão regular digitada
print(re.sub(r"teste", "ABCD", string, count=1))

regexp = re.compile(r"teste")
regexp.search(string)
regexp.findall(string)
regexp.sub("ABCD", string)