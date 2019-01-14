#!/usr/bin/env python3
import json
import os
import threading
from queue import Queue
from getpath import getpath


def addto3(xx):
    l = len(xx)
    if l == 1:
        return "00" + xx
    elif l == 2:
        return "0" + xx
    elif l == 3:
        return xx
    return "000"


tq = Queue(32)

path = getpath('..')
userName = open(os.path.join(path, 'set/userName')).read().strip('\n')

js = json.load(open(os.path.join(path, 'set/info.json')))

homedir = '/home/' + userName + '/'

wacc = 'echo "account:  t{id}" > {fn}'
wpwd = 'echo "password: {pwd}" >> {fn}'
pscp = 'scp -o ConnectTimeout=1 {fn} {sscmd}:' + homedir + 'Desktop/account2longin.txt'


def main(ssname, xx):
    tq.put(ssname)
    filename = os.path.join(path, '.cache/account2longin') + xx['location'] + '.txt'

    os.system(wacc.format(id=addto3(xx['externalid']), fn=filename))
    os.system(wpwd.format(pwd=xx['password'][0], fn=filename))
    os.system(pscp.format(fn=filename, sscmd=ssname))
    os.system('ssh -o ConnectTimeout=1 "chown {un}:{un} /home/{un} -R"'.format(un=userName))

    print(xx["ip"] + ": success.")
    over = tq.get()
    print("release {}".format(over))


for xx in js:
    ssname = 'root@' + xx['ip']
    try:
        threading.Thread(target=main, args=(ssname, xx)).start()
    except:
        print(xx["ip"] + ": failed.")

