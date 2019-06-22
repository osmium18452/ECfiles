#!/usr/bin/env bash

echo "input ip"
read .a

echo "root@"$a > .a

pssh -h .a -t 2 'killall php'
pssh -h .a -t 2 'nohup /opt/domjudge/judgehost/bin/judgedaemon 2 &'
