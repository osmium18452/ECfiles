#!/usr/bin/env bash

dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd $dir

# FIXME this make some errors
for xx in `cat ./iplist`; do
    no=${xx:15}
    ssh $xx "sed -i 's/jud$no/jud/' /opt/domjudge/judgehost/etc/restapi.secret"
    ssh $xx "sed -i 's/jud$nopass/judpass/' /opt/domjudge/judgehost/etc/restapi.secret"
done
