#!/usr/bin/env python3
import os
import json
import threading
from queue import Queue
from getpath import getpath

tq = Queue(32)
path = getpath('../set')

js = json.load(open(os.path.join(path, 'info.json')))

hostname = 'ssh -o ConnectTimeout=1 {sscmd} "hostname {hn}"'
desktop = 'scp -o ConnectTimeout=1 {file} \
        {sscmd}:/usr/share/backgrounds/ICPCLogo-on-dark-smaller.png'
filename = os.path.join(path, 'pic/{}.png')


def main(sscmd, xx):
    print(sscmd)
    tq.put(sscmd)
    os.system(hostname.format(sscmd=sscmd, hostname=xx['location']))
    os.system(desktop.format(file=filename.format(xx['schoolName'][0]), sscmd=sscmd))
    print(xx['ip'] + ': success.')
    over = tq.get()
    print('release {}'.format(over))


for xx in js:
    sscmd = 'root@' + xx['ip']
    try:
        threading.Thread(target=main, args=(sscmd, xx)).start()
    except:
        print(xx['ip'] + ': failed.')
