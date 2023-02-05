import re

ips = """
ONLINE 192.168.0.1 GHIJK active
OFFLINE 192.168.0.2 GHIJK inactive
OFFLINE 192.168.0.3 GHIJK active
ONLINE 192.168.0.4 GHIJK active
ONLINE 192.168.0.5 GHIJK inactive
OFFLINE 192.168.0.6 GHIJK active
"""
# ?= Positive Lookahead
# \w+(?<=) Positive Lookbehind
# ?! Negative Lookahead
# \w+(?<!) Negative Lookbehind

print(re.findall(r"(?:\d{3}.){2}\d.\d", ips, re.I))
print(re.findall(r"[^ \n\r\v\t\fa-z]+", ips, re.I))

# Positive Lookahead
print(re.findall(r"\w+\s+((?:\d+.){3}\d+)\s+\w+\s+(?=active)", ips, re.I))
print(re.findall(r"(?=.*[^in]active).+", ips, re.I))
print(re.findall(r"(?=.*[in]active).+", ips, re.I))

# Negative Lookahead
print(re.findall(r"\w+\s+((?:\d+.){3}\d+)\s+\w+\s+(?!active)", ips, re.I))

#Positive Lookbehind
print(re.findall(r"\w+(?<=ONLINE)\s+((?:\d+.){3}\d+)\s+\w+\s+\w+", ips, re.I))

#Negative Lookbehind
print(re.findall(r"\w+(?<!ONLINE)\s+((?:\d+.){3}\d+)\s+\w+\s+\w+", ips, re.I))