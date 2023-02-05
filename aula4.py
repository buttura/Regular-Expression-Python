# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
import re

texto = '''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div></div>
'''
print(re.findall(r"<[a-zA-Z]*>([a-z-A-Z0-9 _.+-]*)</[a-zA-Z]*>", texto, flags=re.I))
# OU
print(re.findall(r"<[pidv]{1,3}>(.*?)</[pidv]{1,3}>", texto, flags=re.I))

