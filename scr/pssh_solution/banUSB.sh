#!/usr/bin/env bash

dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

cd $dir/../..

command='mkdir /etc/bak -p && mv /lib/modules/`uname -r`/kernel/drivers/usb/storage/ /lib/modules/`uname -r`/kernel/drivers/usb/storage.bak'

parallel-ssh -t 1 -h ./iplist -v $command
parallel-ssh -t 1 -h ./iplist -v "chmod 000 /media -R"
