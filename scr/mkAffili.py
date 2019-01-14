#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from getpath import getpath

path = getpath('../set')

school = open(os.path.join(path, 'JoinedSchool'), 'r')

res = open(os.path.join(path, 'affili.sql'), 'w')

res.write('INSERT INTO `team_affiliation` \
    (`externalid`, `shortname`, `name`, `country`, `comments`) VALUES\n')

ch_en = json.load(open(os.path.join(path, 'SchoolNameCH_EN.json')))
info = json.load(open(os.path.join(path, 'SchoolInfo.json')))

cnt = 1

for xx in school:
    if xx == '\n' or xx == '':
        continue
    if xx[-1:] == '\n':
        xx = xx[:-1]
    enname = ch_en[xx]

    try:
        shortname, country = info[enname][0], info[enname][1]
        cs = '(NULL, "' + shortname + '", "' + enname + '", "' + country + '", ' + 'NULL),\n'
    except KeyError:
        cs = '(NULL, NULL' + ', "' + enname + '", NULL, ' + 'NULL),\n'

    res.write(cs)

res.close()
