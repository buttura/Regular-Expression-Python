import re

string = str(input("Digite o seu email: ")).lower()
re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.+-]+\.[a-zA-Z0-9_.+-]", string)

email = re.compile(r"([a-zA-Z0-9_.+-]+)@[a-zA-Z0-9_.+-]+\.[a-zA-Z0-9_.+-]+")

print(email.search(string))
print(email.findall(string))
print(email.sub("teste", string))