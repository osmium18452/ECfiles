#!/usr/bin/env python3

import os
import json
import functools
import subprocess
import selenium.common
from time import sleep
from selenium import webdriver

os.system('killall phantomjs')
os.system('mkdir -p ./res')
with open('./auth', 'w') as f:
    for i in "qwertyuiopasdfghjklzxcvbnm":
        f.write(i + '\n')

service_args = [
    '--proxy=localhost:1080',
    '--proxy-type=socks5',
]
d = webdriver.PhantomJS(service_args=service_args)
d.get('https://icpc.baylor.edu/')

while True:
    try:
        d.find_element_by_xpath('//*[contains(text(), "Login")]').click()
        break
    except selenium.common.exceptions.NoSuchElementException:
        sleep(1)
while True:
    try:
        d.find_element_by_id('username').send_keys('642191352@qq.com')
        d.find_element_by_id('password').send_keys('zxcvbnm1234567')
        d.find_element_by_class_name('button').click()
        break
    except selenium.common.exceptions.NoSuchElementException:
        sleep(1)

while True:
    try:
        d.find_element_by_xpath('//*[contains(text(), "My Dashboard")]')
        break
    except selenium.common.exceptions.NoSuchElementException:
        sleep(1)


def get_auth():
    auth = ""
    log = json.loads(d.get_log('har')[0].get('message')).get('log').get('entries')
    for r in reversed(log):
        flg = False
        for i in r.get('request').get('headers'):
            if i.get('name') == "Authorization":
                auth = i.get('value')
                flg = True
                break
        if flg:
            break
    with open('./auth', 'w') as f:
        f.write(auth.strip('\n'))


get_auth()
res = subprocess.call(["./robot.sh", ], shell=True)

while True:
    if len(os.listdir('./res')) == 26:
        direct = {}
        for f in os.listdir('./res'):
            if f[-3:] != 'txt':
                continue
            js = json.load(open('./res/' + f))
            for obj in js:
                direct[obj['id']] = obj
        l = []
        for i in direct:
            l.append(direct[i])
        l.sort(key=functools.cmp_to_key(lambda a, b: a['id'] - b['id']))

        with open('result.json', 'w') as f:
            json.dump(l, f, ensure_ascii=False, indent=4)
        d.close()
        break
    sleep(3)

os.system('rm ./auth')
os.system('rm -rf ./res')
os.system('rm ./dict')
