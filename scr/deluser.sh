#!/usr/bin/env bash

dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

cd $dir/..

userName=`cat ./set/userName`

parallel-ssh -t 1 -h ./iplist -v "userdel -r $userName"
