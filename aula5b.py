import re

texto = "<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>"
print(re.findall(r"<(?P<tag>.+?)>(.*?)</(?P=tag)>", texto, flags=re.I))
print(re.sub(r"(<(?P<tag>.+?)>)(.*?)(</(?P=tag)>)", r"\1\3\4", texto, flags=re.I))

cpf = "127.867.546-32"
print(re.findall(r"((?:[0-9]{3}.){2}[0-9]{3}-[0-9]{2})", cpf))
print(re.sub(r"([0-9]{3}).([0-9]{3}).([0-9]{3})-([0-9]{2})", r"\1\2\3\4", cpf))
