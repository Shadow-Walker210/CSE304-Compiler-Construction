# Pattern Matching using RegEx
# (0+1)*+0*1*

import re
str = 'aacc to abcd'
regex = '[(a|b)*(c|d)*]+' or 'ab*c*d'
mon = re.findall(regex , str)
print(mon)



