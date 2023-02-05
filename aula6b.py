import re

cpf = "124.534.565-47"
print(re.findall(r"^((?:[0-9]{3}.){2}[0-9]{3}-[0-9]{2})$", cpf, flags=re.I))
print(re.sub(r"(^[0-9]{3}).([0-9]{3}).([0-9]{3})-([0-9]{2})$", r"\1\2\3\4", cpf, flags=re.I))
print(re.findall(r"[^a-zA-Z.+-]+", cpf, flags=re.I))
print(re.findall(r"((?:[0-9]{3}.){2}[0-9]{3}-[0-9]{2})", cpf, flags=re.I))
print(re.findall(r"((?:\d{3}.){2}\d{3}-\d{2})", cpf, flags=re.I))

texto = "<p>TESTE 1</p> <p>TESTE 2</p> <p>TESTE 3</p> <div>TESTE 4</div>"
print(re.sub(r"<(.+?)>(.*?)</\1>", r"\2", texto, flags=re.I))
print(re.findall(r"<([pidv]{1,3})>(.*?)</\1>", texto, flags=re.I))
