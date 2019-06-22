#!/usr/bin/env bash

dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd $dir

pssh -h ./ipList -t 2 "hostname \`ip a | grep 192.168 | awk '{print \$2}' | cut -d\/ -f1 | sed -e 's/\./\-/g'\`"
