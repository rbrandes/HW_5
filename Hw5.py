import re

with open('regex_sum_38661.txt') as text:
	line = text.read()
y = re.findall('([0-9]+)',line)

print (sum(map(int, y)))
