#!/usr/bin/env bash

dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd $dir

parallel-ssh -h ./iplist "nohup /opt/domjudge/judgehost/bin/judgedaemon 4 &"
