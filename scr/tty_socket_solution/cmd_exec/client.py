#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import socket
import datetime
from time import sleep

# global config
server_info = ('192.168.0.101', 23333)

log_path_prefix = '/var/log/cmd_exec'
os.system('mkdir -p ' + log_path_prefix)
os.system('chmod 600 -R ' + log_path_prefix)

# log config
log_file_path = log_path_prefix + '/cmd_client.log'
log_file = open(log_file_path, 'a+')

# seat config
seat_file_path = '/etc/seat'

# cmd history
cmd_his_file_path = log_path_prefix + '/cmd_his'
try:
    cmd_his = json.load(open(cmd_his_file_path))
except (json.decoder.JSONDecodeError, FileNotFoundError):
    cmd_his = {}

cmd_his_file = open(cmd_his_file_path, 'w+')
json.dump(cmd_his, cmd_his_file)
cmd_his_file.flush()


def log(msg):
    """
    log message
    :param msg: message to log
    """
    log_time = datetime.datetime.now().strftime('[\033[0;32;1m%y-%m-%d %H:%M:%S\033[0m]')
    log_content = log_time + ' ' + msg

    print(log_content, file=log_file)
    log_file.flush()


def save_cmd_history(cmd_history):
    cmd_his_file.seek(0)
    json.dump(cmd_history, cmd_his_file)
    cmd_his_file.flush()


def get_seat_nr():
    """
    :return: seat number
    """
    try:
        seat_nr = open(seat_file_path).read().strip()
        log('get seat number {}'.format(seat_nr))
        return seat_nr
    except FileNotFoundError:
        return ''


def get_cmd():
    """
    send seat number to server and get the command list to execute
    :return: command list to execute {'command number':'command'}
    """
    # create connection
    soc = socket.socket()
    soc.connect(server_info)

    log('connect to {}:{}'.format(*server_info))

    # send seat number
    soc.sendall(get_seat_nr().encode())

    # get cmd to exec
    cmd_recv = soc.recv(2147483647).decode()
    log('cmd received')

    # exit
    log('disconnect')
    soc.send('exit'.encode())
    soc.close()
    return json.loads(cmd_recv)


def exec_cmd(cmd_dict):
    """
    to execute the command list
    :param cmd_dict: command list {'command number':'command'}
    """
    global cmd_his
    for cmd_nr in cmd_dict:
        if cmd_his.get(cmd_nr) != cmd_dict[cmd_nr]:
            cmd_to_exec = cmd_dict[cmd_nr]

            log('exec command: {}'.format(cmd_to_exec))
            os.system(cmd_to_exec)

            cmd_his[cmd_nr] = cmd_to_exec
            save_cmd_history(cmd_his)


if __name__ == '__main__':
    while True:
        try:
            exec_cmd(get_cmd())
        except ConnectionRefusedError:
            log('connection refused...')
        except OSError:
            log('network unreachable...')
        sleep(60)
