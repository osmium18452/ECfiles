import json
import os
from getpath import getpath

path = getpath('../../set/')

with open(os.path.join(path, 'info.json')) as f:
    teams = json.load(f)

tmp = "update team set room = '{}' where teamid = {};"

with open(os.path.join(path, 'loc.sql'), 'w+') as f:
    for team in teams:
        print(tmp.format(
            team['location'],
            team['id']
        ), file = f)
