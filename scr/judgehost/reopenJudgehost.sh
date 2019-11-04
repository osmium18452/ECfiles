#!/usr/bin/env bash

printf "Input IP: 192.168."
read a

echo "root@192.168."$a > .a

pssh -h .a -t 2 'killall php'
pssh -h .a -t 2 'nohup /opt/domjudge/judgehost/bin/judgedaemon 2 &'
