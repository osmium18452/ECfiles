#!/usr/bin/env bash

dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

cd $dir/..

ct=`date +"%H:%M:%S %Y-%m-%d"`

parallel-ssh -t 0 -h ./iplist -v "date -s \"$ct\" &"
