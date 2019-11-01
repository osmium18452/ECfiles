#!/usr/bin/env bash

dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

cd $dir/../..

userName=`cat ./set/userName`
passwd=`cat ./set/passwd`

parallel-ssh -t 1 -h ./iplist  -v "useradd $userName -m -s /bin/bash &"
parallel-ssh -t 1 -h ./iplist  -v "echo $passwd > passwd && echo $passwd >> passwd"
parallel-ssh -t 1 -h ./iplist  -v "cat passwd | passwd $userName && rm passwd"
parallel-ssh -t 1 -h ./iplist  -v "mkdir -p /home/$userName/.vscode && chown $userName:$userName /home/$userName/.vscode -R"
parallel-ssh -t 1 -h ./iplist  -v "ln -sf /home/acm/.vscode/extensions /home/$userName/.vscode/extensions"
