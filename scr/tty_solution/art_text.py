import re
import json
import string
from art import *

x = string.ascii_uppercase + string.digits + '-'
res = {}

for i in x:
    s = re.sub(r'[^\n\s]', '█', text2art(i, font='doh'))
    s = s.replace('\r', '').split('\n')
    res[i] = s

print(res)
with open('art.json', 'w') as f:
    json.dump(res, f, indent=4, ensure_ascii=False)
