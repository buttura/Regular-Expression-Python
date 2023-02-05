import re

numeros = """
0.0
00.00
000.000
+0.0
-00.00
+000.000
10
50
8.5
-8.5
+10.5005412136
1231345458.54654564
-1332156456589.6543215648978977
+1.11123123

++1213
--1235050
.124546
-.1231324
10.
.1
.10
10.
+10.
-10.
5a
b5
"""

print(re.findall(r"^[+]?(?!-)[0-9]+.?[0-9]+$", numeros, flags=re.M))
print(re.findall(r"^[+-]?[0-9]+(?:.[0-9]+)?$", numeros, flags=re.M))


def inteiro(string):
    return bool(re.search(r"^[+-]?\d+$", string, flags=re.M))


def flutuantes(string):
    return bool(re.search(r"^[+-]?\d+.\d+$", string, flags=re.M))


while True:
    numero = str(input("Digite um número: "))
    if inteiro(numero):
        print("É inteiro!")
    else:
        print("É flutuante")
