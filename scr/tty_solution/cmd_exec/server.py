#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import socket
import datetime
import threading


# global config
server_info = ('0.0.0.0', 23333)
max_conn_nbr = 1000

log_path_prefix = '/var/log/cmd_exec'
os.system('mkdir -p ' + log_path_prefix)

# log config
log_file_path = log_path_prefix + '/cmd_server.log'
log_file = open(log_file_path, 'a+')
lock_log = threading.Lock()
logs = ''

# ip:seat config
seat_ip_file_path = 'ip_seat.json'
seat_ip_file = open(seat_ip_file_path, 'w+')
lock_seat_ip = threading.Lock()
try:
    seat_ip = json.load(seat_ip_file)
except json.decoder.JSONDecodeError:
    seat_ip = {}

# cmd list
cmd_list_file_path = 'cmd_list'
try:
    cmd_list = json.load(open(cmd_list_file_path))
except (json.decoder.JSONDecodeError, FileNotFoundError):
    cmd_list = {}
cmd_cnt = len(cmd_list)

cmd_list_file = open(cmd_list_file_path, 'w+')
json.dump(cmd_list, cmd_list_file)
cmd_list_file.flush()

lock_cmd_list = threading.Lock()


def log(msg):
    """
    log message
    :param msg: message to log
    """
    global lock_log, logs
    log_time = datetime.datetime.now().strftime('[\033[0;32;1m%y-%m-%d %H:%M:%S\033[0m]')
    log_content = log_time + ' ' + msg

    lock_log.acquire()
    try:
        print(log_content, file=log_file)
        log_file.flush()
    finally:
        lock_log.release()


def get_cmd():
    """
    get cmd to exec
    """
    global cmd_cnt, cmd_list, lock_cmd_list
    while True:
        try:
            cmd_new = input('CMD[{}] > '.format(format(cmd_cnt, '0>3')))

            lock_cmd_list.acquire()
            try:
                cmd_list[cmd_cnt] = cmd_new
                cmd_cnt += 1

                cmd_list_file.seek(0)
                json.dump(cmd_list, cmd_list_file)
                cmd_list_file.flush()
            finally:
                lock_cmd_list.release()
        except (KeyboardInterrupt, EOFError):
            print()
            continue


def update_seat_info(seat_nr, ip_addr):
    """
    :param seat_nr: seat number
    :param ip_addr: ip address
    """
    global seat_ip, lock_seat_ip
    lock_seat_ip.acquire()
    try:
        seat_ip[seat_nr] = {
            'ip': ip_addr,
            'time': datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
        }

        seat_ip_file.seek(0)
        json.dump(seat_ip, seat_ip_file)
        seat_ip_file.flush()
    finally:
        lock_seat_ip.release()


def link_handler(link, client):
    """
    function to handle a connection
    :param link: link information
    :param client: (ip, port) for client
    """
    global lock_cmd_list
    log('conn from {}:{} start'.format(client[0], client[1]))

    lock_cmd_list.acquire()
    try:
        cmd = json.dumps(cmd_list)
    finally:
        lock_cmd_list.release()

    while True:
        # get and update seat
        seat = link.recv(128).decode()
        log('{} -- {}'.format(client[0], seat))
        update_seat_info(seat_nr=seat, ip_addr=client[0])

        # send cmd
        link.sendall(cmd.encode())
        ret = link.recv(128).decode().strip()

        # waiting for exit
        if ret == 'exit':
            log('conn from {}:{} exit'.format(client[0], client[1]))
            link.close()
            return


if __name__ == '__main__':
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind(server_info)
    soc.listen(max_conn_nbr)

    log('start listen')

    threading.Thread(target=get_cmd).start()

    while True:
        conn, addr = soc.accept()
        threading.Thread(target=link_handler, args=(conn, addr)).start()
