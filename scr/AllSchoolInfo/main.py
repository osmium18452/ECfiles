#!/usr/bin/env python3

import os
import json
import functools
import subprocess
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

username = ''
password = ''


def waiting_for(d, elem):
    while True:
        try:
            d.find_element_by_xpath(elem)
            break
        except NoSuchElementException:
            sleep(1)
    return d.find_element_by_xpath(elem)


def get_auth():
    service_args = [
        '--proxy=localhost:1080',
        '--proxy-type=socks5',
    ]
    os.system('killall phantomjs')
    d = webdriver.PhantomJS(service_args=service_args)
    d.implicitly_wait(60)
    d.get('https://icpc.baylor.edu/')
    waiting_for(d, '//*[contains(text(), "Login")]').click()
    d.find_element_by_id('username').send_keys(username)
    d.find_element_by_id('password').send_keys(password)
    d.find_element_by_class_name('button').click()

    waiting_for(d, '//*[contains(text(), "My Dashboard")]')
    log = json.loads(d.get_log('har')[0].get('message')).get('log').get('entries')
    d.close()

    for r in log[::-1]:
        for header in r.get('request').get('headers'):
            if header.get('name') == "Authorization":
                with open('./auth', 'w') as f:
                    print(header.get('value'), file=f, end='')
                return


if __name__ == '__main__':
    get_auth()
    res = subprocess.call(["./robot.sh", ], shell=True)
    while True:
        if len(os.listdir('./res')) == 26:
            res = list({j['id']: j for f in os.listdir('./res') for j in json.load(open('./res/' + f))}.values())
            res.sort(key=functools.cmp_to_key(lambda a, b: a['id'] - b['id']))
            with open('result.json', 'w') as f:
                json.dump(res, f, ensure_ascii=False, indent=4)
            break
        print("waiting for robot...")
        sleep(3)
    os.system('rm -rf ./auth ./dict ./res ./ghostdriver.log')
