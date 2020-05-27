import re
s = 0
file = open("regex_sum_504388.txt")
for line in file:
    lst = re.findall('[0-9]+', line)
    for i in lst:
        s = s+int(i)
print(s)
