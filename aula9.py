import re

cpf = "025.258.963-10"
cpfRegExp = re.compile(r"^(\d{3}.){2}\d{3}-\d{2}$")
print(cpfRegExp.search(cpf))

ipRegExp = re.compile(r'''
    ^
    (?:
        (?:
            25[0-5]| # 250-255
            2[0-4][0-9]| # 200-249
            [0-1][0-9]{2}| # 100-199
            [1-9][0-9]| # 10-99
            [0-9] # 0-9
        )
        \.?
    ){4}
    \b
    $
''', flags=re.X)

for i in range(300+1):
    ip = f"{i}.{i}.{i}.{i}"
    print(ip, ipRegExp.findall(ip))