#!/usr/bin/env python3
import json
import os
from getpath import getpath

path = getpath('../../set')

with open(os.path.join(path, 'info.json')) as f:
    teams = json.load(f)

ID = json.load(open(os.path.join(path, 'sname2id.json')))

tmp = "update team set affilid = '{}' where teamid = {};"

with open('loc.sql', 'w+') as f:
    for team in teams:
        print(tmp.format(
            ID[team['schoolName'][1]],
            team['id']
        ), file=f)
