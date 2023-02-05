import re
# 698.547.520-54
def ValidarCPF(texto):
    FormatoCPF = re.compile(r"^((?:\d{3}\.){2}\d{3}-\d{2})$", flags=re.I | re.X)
    s = 0
    while True:
        cpfUsuario = str(input(texto))
        cpfUsuario = re.sub(r"^(\d{3})\.?(\d{3})\.?(\d{3})-?(\d{2})$", r"\1.\2.\3-\4", cpfUsuario, flags=re.X | re.I)
        Resultado = False
        if len(FormatoCPF.findall(cpfUsuario)) != 0:
            for i in range(1000):
                cpf = f"{i}.{i}.{i}-{i//10}"
                cpfInvalido = FormatoCPF.findall(cpf)
                if cpfUsuario in cpfInvalido:
                    Resultado = True
                    break
        else:
            Resultado = True
        if Resultado:
            s += 1
            print(f"({s}) CPF Inválido, Tente novamente.", end=" ")
        else:
            return cpfUsuario


print(ValidarCPF("Digite o CPF: "))

#ou
FormatoCPF2 = re.compile(r"^(?!(\d)\1{2}\.?\1{3}\.?\1{3}-?\1{2})((?:\d{3}\.?){3}-?\d{2})$", flags=re.M | re.I)
print(FormatoCPF2.findall(str(input("Digite o CPF: "))))