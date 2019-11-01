#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
import os
from getpath import getpath

path = getpath('../set')

js = json.load(open(os.path.join(path, "info.json"), "r"))
teams = open(os.path.join(path, "teams.tab"), "w")
accounts = open(os.path.join(path, "accounts.tab"), "w")

info = json.load(open(os.path.join(path, "SchoolInfo.json")))


def eraseZ(xx):
    i = 0
    while True:
        if xx[i] != '0':
            break
        i = i + 1
    return xx[i:]


def addto3(xx):
    return format(xx, '0>3')


ID = {
    "regular": "3",
    "girl": "7",
    "star": "8",
    "post-graduate": "9",
}


teams.write('teams\t1\n')
accounts.write('accounts\t1\n')

pd = 0 if len(sys.argv) == 1 else 1

for xx in js:
    sname = xx['schoolName'][1]
    shortname, country = "", "CHN"
    try:
        shortname, country = info[sname][0], info[sname][1]

        teamStr = ""
        teamStr = teamStr + eraseZ(xx["externalid"]) + '\t'
        teamStr = teamStr + addto3(xx["externalid"]) + '\t'
        teamStr = teamStr + ID[xx["mark"]] + '\t'
        teamStr = teamStr + xx["name"][0] + '(' + xx['name'][1] + ')\t'
        teamStr = teamStr + sname + '\t'
        teamStr = teamStr + shortname + '\t'
        teamStr = teamStr + country
        teams.write(teamStr + '\n')

        accStr = "team\t\t"
        accStr = accStr + "t" + addto3(eraseZ(xx["externalid"])) + '\t'
        accStr = accStr + xx["password"][1]
        accounts.write(accStr + '\n')

    except KeyError:
        pass
    print(xx['id'], "done.")
