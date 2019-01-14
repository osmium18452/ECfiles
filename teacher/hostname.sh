#!/usr/bin/env bash

dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd $dir

for xx in `cat ./ipteacher`; do
    no=${xx:15}
    ssh $xx "hostname PC-$no &"
done
