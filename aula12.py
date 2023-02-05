import random

QuantidadeDeCaracteres = int(input("Digite a quantidade de caracteres: "))
print("\n", end="")


def glyph47():
    return chr(random.randint(33, 47))


def glyph57():
    return chr(random.randint(48, 57))


def glyph90():
    return chr(random.randint(65, 90))


def glyph122():
    return chr(random.randint(97, 122))


def criarsenha(largura=QuantidadeDeCaracteres, maiusculo=True, minusculo=True, numeros=True, characters=True):
    senhagerada = []
    for _ in range(largura):
        if maiusculo:
            senhagerada.append(glyph90())
        if minusculo:
            senhagerada.append(glyph122())
        if numeros:
            senhagerada.append(glyph57())
        if characters:
            senhagerada.append(glyph47())
        if len(senhagerada) > largura:
            for _ in range(len(senhagerada) - largura):
                senhagerada.pop()
    random.shuffle(senhagerada)
    for Valor in senhagerada:
        print(Valor, end="")


# Senha com todos os Caracteres
print("TODOS OS CARACTERES")
for i in range(5):
    criarsenha()
    print("\n", end="")
print("\n", end="")

# Sem Minúsculas
print("SEM MINÚSCULAS")
for i in range(5):
    criarsenha(12, True, False, True, True)
    print("\n", end="")
print("\n", end="")

# Sem Minúsculas e Números
print("SEM MINÚSCULAS E NÚMEROS")
for i in range(5):
    criarsenha(12, True, False, False, True)
    print("\n", end="")
print("\n", end="")
