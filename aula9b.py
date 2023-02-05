import re


ipRegEx = re.compile(r"^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|\d)\.?){4}\b$", flags=re.X)
for i in range(300+1):
    ip = f"{i}.{i}.{i}.{i}"
    print(ipRegEx.findall(ip))