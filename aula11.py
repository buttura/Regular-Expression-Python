import re

numeros = """
(21) 9 8852-5214
(11) 9955-1231
(35) 9 9975-4521
(31) 3851-2587
9 8571-5213
1234-5647
"""
#print(re.findall(r".*?\s(\d{4}-\d{4})", numeros, flags=re.I))
print(re.findall(r"(\(\d{2}\)\s\d\s\d{4}-\d{4})", numeros, flags=re.I | re.M))

