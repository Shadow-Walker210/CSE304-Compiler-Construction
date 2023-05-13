import re
num = '01'
mon = re.search('[0-1]*$|0*1*', num)
print(mon.group())