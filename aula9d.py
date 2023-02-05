import re
ipRegEx = re.compile(r"^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|\d)\.?){4}\b$", flags=re.X)
for i in range(300+1):
    ip = f"{i}.{i}.{i}.{i}"
    print(re.findall(ipRegEx, ip))

ips = """
ONLINE 192.168.0.1 GHIJK active
OFFLINE 192.168.0.2 GHIJK inactive
OFFLINE 192.168.0.3 GHIJK active
ONLINE 192.168.0.4 GHIJK active
ONLINE 192.168.0.5 GHIJK inactive
OFFLINE 192.168.0.6 GHIJK active
"""

print(re.findall(r"(\w+(?<=online).*)", ips, flags=re.I))
print(re.findall(r"(?<=online)\s+(.*?)\s+", ips, flags=re.I))

print(re.findall(r"\w*\s+((?:\d+\.?){4})\s+\w*\s+(?=inactive)", ips, flags=re.I))
