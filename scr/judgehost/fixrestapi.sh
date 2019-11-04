#!/usr/bin/env bash

dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd $dir

pssh -h ./ipList -t 2 "echo default http://192.168.0.101/domjudge/api/ j1 123456 > /opt/domjudge/judgehost/etc/restapi.secret"
