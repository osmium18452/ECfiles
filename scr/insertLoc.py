# _*- coding: utf-8 -*-

import json
import os
from getpath import getpath

path = getpath('../set')

tmp = 'update team set room = "{}" where teamid={};'

with open(os.path.join(path, 'info.json')) as f:
    teams = json.load(f)

with open(os.path.join(path, 'room.sql'), 'w+') as f:
    for team in teams:
        t = tmp.format(team['location'], team['id'])
        print(t, file=f)
